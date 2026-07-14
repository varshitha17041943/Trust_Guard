import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Globe, ArrowRight, ShieldCheck, Search, CheckCircle2, Loader2, AlertTriangle } from 'lucide-react';
import api from '../utils/axios'; // Wait, SSE usually needs standard fetch or EventSource if it's a GET, but for POST we use fetch.

const WebsiteScanner = () => {
  const [url, setUrl] = useState('');
  const [isScanning, setIsScanning] = useState(false);
  const [logs, setLogs] = useState<{message: string, type: 'start' | 'complete' | 'error'}[]>([]);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleScan = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!url) return;
    setIsScanning(true);
    setLogs([]);
    setError('');

    try {
      const token = localStorage.getItem('access_token');
      const baseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';
      const response = await fetch(`${baseUrl}/scan/url`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ target_url: url })
      });

      if (!response.ok) throw new Error("Stream failed to initialize");
      
      const reader = response.body?.getReader();
      const decoder = new TextDecoder();
      
      if (!reader) throw new Error("No stream reader");

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        
        const chunk = decoder.decode(value, { stream: true });
        const lines = chunk.split('\n\n');
        
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = JSON.parse(line.slice(6));
            if (data.event === 'step_start') {
              setLogs(prev => [...prev, { message: data.step, type: 'start' }]);
            } else if (data.event === 'step_complete') {
              setLogs(prev => [...prev, { message: data.step, type: 'complete' }]);
            } else if (data.event === 'partial_failure') {
              setLogs(prev => [...prev, { message: data.step, type: 'error' }]);
            } else if (data.event === 'completed') {
              setTimeout(() => navigate(`/app/results/${data.scan_id}`), 1000);
            }
          }
        }
      }
    } catch (err: any) {
      setError(err.message || 'Scanning interrupted');
      setIsScanning(false);
    }
  };

  return (
    <div className="max-w-3xl mx-auto space-y-8">
      <div className="text-center space-y-4 mb-12">
        <div className="w-16 h-16 mx-auto bg-primary/20 rounded-full flex items-center justify-center">
          <Globe className="text-primary w-8 h-8" />
        </div>
        <h1 className="text-3xl font-bold">Website Scanner</h1>
        <p className="text-gray-400">Powered by Antigravity Multi-Agent Workflow.</p>
      </div>

      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="glass-panel p-8">
        <form onSubmit={handleScan} className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">Target URL</label>
            <div className="relative">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-500 w-5 h-5" />
              <input 
                type="url" required placeholder="https://example.com"
                className="w-full bg-surface border border-border rounded-xl pl-12 pr-4 py-4 text-white focus:outline-none focus:border-primary"
                value={url} onChange={(e) => setUrl(e.target.value)} disabled={isScanning}
              />
            </div>
          </div>

          {error && <div className="text-danger text-sm bg-danger/10 p-3 rounded">{error}</div>}

          {!isScanning ? (
            <button type="submit" className="w-full btn-primary flex items-center justify-center gap-2 py-4 text-lg">
              Start Analysis <ArrowRight size={20} />
            </button>
          ) : (
            <div className="relative rounded-2xl overflow-hidden bg-background/50 border border-border p-6 min-h-[300px] flex flex-col justify-end shadow-[inset_0_0_50px_rgba(59,130,246,0.1)]">
              {/* Radar Effect Background */}
              <div className="absolute inset-0 flex items-center justify-center opacity-30 pointer-events-none">
                <div className="w-full h-full border-t border-primary/50 rounded-full animate-spin [animation-duration:3s]" style={{ width: '150%', height: '150%', transformOrigin: 'center' }}></div>
              </div>
              <div className="absolute inset-0 bg-gradient-to-t from-background via-transparent to-transparent pointer-events-none"></div>

              <div className="space-y-4 font-mono text-sm relative z-10 overflow-y-auto max-h-[250px] pr-2">
                {logs.map((log, idx) => (
                  <motion.div key={idx} initial={{ opacity: 0, x: -20, filter: 'blur(5px)' }} animate={{ opacity: 1, x: 0, filter: 'blur(0px)' }} transition={{ duration: 0.3 }} className="flex items-center gap-3">
                    {log.type === 'start' && (
                      <span className="relative flex h-3 w-3">
                        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75"></span>
                        <span className="relative inline-flex rounded-full h-3 w-3 bg-primary"></span>
                      </span>
                    )}
                    {log.type === 'complete' && <CheckCircle2 className="text-success shrink-0" size={16} />}
                    {log.type === 'error' && <AlertTriangle className="text-danger shrink-0" size={16} />}
                    <span className={log.type === 'start' ? 'text-primary animate-pulse' : log.type === 'error' ? 'text-danger' : 'text-success font-medium'}>
                      {log.message}
                    </span>
                  </motion.div>
                ))}
              </div>
            </div>
          )}
        </form>
      </motion.div>
    </div>
  );
};

export default WebsiteScanner;
