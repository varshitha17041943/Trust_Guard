import React, { useState } from 'react';

export const ChatAssistant = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([{role: 'ai', text: 'Hi! Ask me anything about phishing, SSL, or scams.'}]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    if (!input) return;
    setMessages(prev => [...prev, { role: 'user', text: input }]);
    const currentInput = input;
    setInput('');
    
    // Call RAG backend
    const res = await fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({query: currentInput, session_id: '123'})
    });
    const data = await res.json();
    setMessages(prev => [...prev, { role: 'ai', text: data.answer }]);
  };

  if (!isOpen) {
    return (
      <button 
        onClick={() => setIsOpen(true)}
        className="fixed bottom-4 right-4 bg-blue-600 text-white p-4 rounded-full shadow-lg hover:bg-blue-700 transition"
      >
        Ask AI
      </button>
    );
  }

  return (
    <div className="fixed bottom-4 right-4 w-80 h-96 bg-gray-900 border border-gray-700 rounded-lg shadow-xl flex flex-col">
      <div className="p-4 bg-gray-800 border-b border-gray-700 flex justify-between items-center rounded-t-lg">
        <h3 className="text-white font-bold">Cyber Security AI</h3>
        <button onClick={() => setIsOpen(false)} className="text-gray-400 hover:text-white">✕</button>
      </div>
      <div className="flex-1 p-4 overflow-y-auto flex flex-col gap-2">
        {messages.map((m, i) => (
          <div key={i} className={`p-2 rounded-lg max-w-[80%] ${m.role === 'ai' ? 'bg-gray-800 text-gray-200 self-start' : 'bg-blue-600 text-white self-end'}`}>
            {m.text}
          </div>
        ))}
      </div>
      <div className="p-2 border-t border-gray-700 flex">
        <input 
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Ask about SSL..."
          className="flex-1 bg-gray-800 text-white p-2 rounded-l focus:outline-none"
        />
        <button onClick={handleSend} className="bg-blue-600 text-white p-2 rounded-r">Send</button>
      </div>
    </div>
  );
};
