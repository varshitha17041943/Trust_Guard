import os

def create_files():
    files = {
        "frontend/src/components/ChatAssistant.tsx": """import React, { useState } from 'react';

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
""",
        "frontend/src/pages/AdminDashboard.tsx": """import React, { useEffect, useState } from 'react';

export const AdminDashboard = () => {
    const [stats, setStats] = useState({total_users: 0, total_scans: 0, blocked_urls: 0, active_threats: 0});
    
    useEffect(() => {
        fetch('/api/admin/stats')
            .then(res => res.json())
            .then(data => setStats(data))
            .catch(err => console.error(err));
    }, []);

    return (
        <div className="min-h-screen bg-black text-white p-8">
            <h1 className="text-3xl font-bold mb-8">Admin Dashboard</h1>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                <div className="bg-gray-900 p-6 rounded-xl border border-gray-800">
                    <h3 className="text-gray-400 text-sm">Total Users</h3>
                    <p className="text-3xl font-bold text-white mt-2">{stats.total_users}</p>
                </div>
                <div className="bg-gray-900 p-6 rounded-xl border border-gray-800">
                    <h3 className="text-gray-400 text-sm">Total Scans</h3>
                    <p className="text-3xl font-bold text-blue-400 mt-2">{stats.total_scans}</p>
                </div>
                <div className="bg-gray-900 p-6 rounded-xl border border-gray-800">
                    <h3 className="text-gray-400 text-sm">Blocked URLs</h3>
                    <p className="text-3xl font-bold text-red-500 mt-2">{stats.blocked_urls}</p>
                </div>
                <div className="bg-gray-900 p-6 rounded-xl border border-gray-800">
                    <h3 className="text-gray-400 text-sm">Active Threats</h3>
                    <p className="text-3xl font-bold text-orange-400 mt-2">{stats.active_threats}</p>
                </div>
            </div>
        </div>
    );
};
""",
        "frontend/src/components/NotificationBell.tsx": """import React, { useEffect, useState } from 'react';

export const NotificationBell = () => {
    const [notifications, setNotifications] = useState([]);
    const [isOpen, setIsOpen] = useState(false);

    useEffect(() => {
        fetch('/api/notifications')
            .then(res => res.json())
            .then(data => setNotifications(data))
            .catch(err => console.error(err));
    }, []);

    const unreadCount = notifications.filter(n => !n.is_read).length;

    return (
        <div className="relative">
            <button 
                onClick={() => setIsOpen(!isOpen)}
                className="relative p-2 text-gray-400 hover:text-white transition"
            >
                🔔
                {unreadCount > 0 && (
                    <span className="absolute top-0 right-0 bg-red-500 text-white text-xs rounded-full h-4 w-4 flex items-center justify-center">
                        {unreadCount}
                    </span>
                )}
            </button>
            {isOpen && (
                <div className="absolute right-0 mt-2 w-80 bg-gray-900 border border-gray-700 rounded-lg shadow-xl z-50">
                    <div className="p-3 border-b border-gray-700 font-bold text-white">Notifications</div>
                    <div className="max-h-64 overflow-y-auto">
                        {notifications.map((n, i) => (
                            <div key={i} className={`p-3 border-b border-gray-800 ${!n.is_read ? 'bg-gray-800' : ''}`}>
                                <p className="text-sm text-gray-300">{n.message}</p>
                            </div>
                        ))}
                        {notifications.length === 0 && <div className="p-3 text-gray-500 text-center">No notifications</div>}
                    </div>
                </div>
            )}
        </div>
    );
};
"""
    }

    for path, content in files.items():
        dirname = os.path.dirname(path)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    create_files()
    print("Frontend Expansion (Stages 21-25) Scaffolded.")
