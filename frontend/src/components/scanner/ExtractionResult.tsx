import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Link2, ShieldAlert, ShieldCheck, ArrowRight, RefreshCw, Loader2 } from 'lucide-react';
import api from '../../utils/axios';
import { useNavigate } from 'react-router-dom';

const ExtractionResult = ({ url, onReset }: { url: string; onReset: () => void }) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleAnalyze = async () => {
    setLoading(true);
    setError('');
    try {
      const formData = new FormData();
      formData.append('extracted_url', url);
      
      const res = await api.post('/scan/qr', formData);
      // Navigate to results page after analysis triggers successfully
      navigate(`/app/results/${res.data.scan_id}`);
    } catch (err: any) {
      setError(err.response?.data?.error || "Failed to trigger analysis. The URL may be fundamentally invalid or unsafe.");
      setLoading(false);
    }
  };

  const isSuspicious = url.toLowerCase().includes('javascript:') || !url.startsWith('http');

  return (
    <motion.div initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} className="text-center space-y-6">
      <div className={`w-20 h-20 mx-auto rounded-full flex items-center justify-center ${isSuspicious ? 'bg-danger/20 text-danger' : 'bg-success/20 text-success'}`}>
        {isSuspicious ? <ShieldAlert size={40} /> : <ShieldCheck size={40} />}
      </div>
      
      <div>
        <h2 className="text-2xl font-bold mb-2">Extracted Payload</h2>
        <div className="bg-surface border border-border rounded-lg p-4 break-all flex items-center gap-3">
          <Link2 className="shrink-0 text-gray-500" />
          <span className="text-lg font-mono text-white">{url}</span>
        </div>
      </div>

      {error && (
        <div className="bg-danger/10 border border-danger text-danger p-4 rounded-lg text-sm text-left">
          {error}
        </div>
      )}

      <div className="flex flex-col sm:flex-row gap-4 pt-4">
        <button onClick={onReset} disabled={loading} className="btn-secondary flex-1 flex items-center justify-center gap-2">
          <RefreshCw size={18} /> Scan Another
        </button>
        <button onClick={handleAnalyze} disabled={loading} className="btn-primary flex-1 flex items-center justify-center gap-2">
          {loading ? <Loader2 className="animate-spin" size={18} /> : <>Analyze Payload <ArrowRight size={18} /></>}
        </button>
      </div>
    </motion.div>
  );
};

export default ExtractionResult;
