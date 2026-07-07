import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { MessageSquare, Send, Bot, User } from 'lucide-react';
import { api } from '../../services/api';

export const Chatbot = () => {
  const [messages, setMessages] = useState([
    { role: 'assistant', content: 'Hello! I am your TrustGuard Cybersecurity Advisor. Ask me anything about phishing, malware, or how to secure your accounts.' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;
    const userMsg = input;
    setMessages(prev => [...prev, { role: 'user', content: userMsg }]);
    setInput('');
    setLoading(true);

    try {
      // Assuming a RAG endpoint
      const res = await api.post('/chatbot/ask', { query: userMsg });
      setMessages(prev => [...prev, { role: 'assistant', content: res.data.answer }]);
    } catch (err) {
      setMessages(prev => [...prev, { role: 'assistant', content: "I'm sorry, my systems are currently offline. Please try again later." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-8 max-w-4xl mx-auto h-[80vh] flex flex-col">
      <h1 className="text-2xl font-bold flex items-center gap-2"><MessageSquare/> Security Advisor (AI)</h1>
      
      <Card className="flex-grow flex flex-col overflow-hidden">
        <div className="flex-grow overflow-y-auto p-6 space-y-6">
          {messages.map((msg, i) => (
            <div key={i} className={`flex gap-4 ${msg.role === 'user' ? 'flex-row-reverse' : ''}`}>
              <div className={`shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${msg.role === 'user' ? 'bg-primary' : 'bg-secondary'}`}>
                {msg.role === 'user' ? <User className="w-5 h-5 text-white" /> : <Bot className="w-5 h-5 text-black" />}
              </div>
              <div className={`max-w-[70%] p-4 rounded-xl ${msg.role === 'user' ? 'bg-primary/20 text-primary-light' : 'bg-white/10 text-white/90'}`}>
                {msg.content}
              </div>
            </div>
          ))}
          {loading && (
            <div className="flex gap-4">
              <div className="shrink-0 w-8 h-8 rounded-full bg-secondary flex items-center justify-center"><Bot className="w-5 h-5 text-black" /></div>
              <div className="max-w-[70%] p-4 rounded-xl bg-white/10 text-white/50 animate-pulse">Thinking...</div>
            </div>
          )}
        </div>
        
        <div className="p-4 border-t border-white/10 bg-background/50 flex gap-2">
          <input 
            type="text" 
            className="flex-grow bg-background border border-white/10 rounded-lg px-4 py-2 focus:outline-none focus:border-primary"
            placeholder="Ask about phishing, recent scans, or general security..."
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && handleSend()}
          />
          <Button onClick={handleSend} disabled={loading}><Send className="w-4 h-4"/></Button>
        </div>
      </Card>
    </div>
  );
};
