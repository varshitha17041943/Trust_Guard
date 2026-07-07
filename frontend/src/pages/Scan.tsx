import React, { useState } from 'react';
import { motion } from 'framer-motion';
import ScanResult from '../components/ScanResult';

const Scan = () => {
  const [url, setUrl] = useState('');
  const [isScanning, setIsScanning] = useState(false);
  const [events, setEvents] = useState<any[]>([]);

  const handleScan = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsScanning(true);
    setEvents([]);
    
    const response = await fetch('http://localhost:8000/scans/stream', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({target_url: url})
    });
    
    const reader = response.body?.getReader();
    const decoder = new TextDecoder();
    
    if (reader) {
        while (true) {
            const {done, value} = await reader.read();
            if (done) break;
            const text = decoder.decode(value);
            const lines = text.split('\n\n').filter(Boolean);
            for (const line of lines) {
                if (line.startsWith('data: ')) {
                    try {
                         // Fix json quotes from python to be valid
                        const payload = line.replace('data: ', '').replace(/'/g, '"');
                        const data = JSON.parse(payload);
                        setEvents(prev => [...prev, data]);
                        if (data.status === 'completed') setIsScanning(false);
                    } catch(e) { console.error(e) }
                }
            }
        }
    }
  };

  return (
    <div className="max-w-4xl mx-auto space-y-8">
      <div className="bg-slate-800 p-8 rounded-2xl border border-slate-700 shadow-2xl relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-sky-500/10 to-indigo-500/10 z-0"></div>
        <div className="relative z-10">
          <h2 className="text-2xl font-bold text-white mb-4">Analyze Target</h2>
          <form onSubmit={handleScan} className="flex gap-4">
            <input 
              type="url" 
              required
              placeholder="https://example.com"
              className="flex-1 bg-slate-900 border border-slate-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-sky-500"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              disabled={isScanning}
            />
            <button 
              type="submit"
              disabled={isScanning}
              className="bg-sky-500 hover:bg-sky-400 text-white px-8 py-3 rounded-lg font-semibold transition disabled:opacity-50"
            >
              {isScanning ? 'Analyzing...' : 'Scan Now'}
            </button>
          </form>
        </div>
      </div>
      
      {events.length > 0 && (
          <ScanResult events={events} />
      )}
    </div>
  );
};

export default Scan;
