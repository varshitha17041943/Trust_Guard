import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { motion } from 'framer-motion';
import { ShieldAlert, ShieldCheck, Download, FileJson, FileText, AlertTriangle, ArrowRight, Lightbulb } from 'lucide-react';
import api from '../utils/axios';

const Results = () => {
  const { id } = useParams();
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchReport = async () => {
      try {
        const res = await api.get(`/report/${id}`);
        setData(res.data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchReport();
  }, [id]);

  const handleDownloadPDF = () => {
    window.open(`/api/report/${id}/download`, '_blank');
  };

  const handleDownloadJSON = () => {
    window.open(`/api/report/${id}/json`, '_blank');
  };

  const handleDownloadMD = () => {
    window.open(`/api/report/${id}/markdown`, '_blank');
  };

  if (loading) return <div className="flex justify-center p-20"><div className="animate-spin rounded-full h-12 w-12 border-t-2 border-primary"></div></div>;
  if (!data) return <div className="text-center p-20">Report not found.</div>;

  const isRisky = data.risk_score > 40;
  const whyExplanations = data.threat_intel?.length > 0 
    ? data.threat_intel.map((t: string) => `This domain triggered a security flag: ${t}`)
    : ["Our security checks found no immediate red flags."];

  return (
    <div className="max-w-4xl mx-auto space-y-8 pb-20">
      {/* Toolbar */}
      <div className="flex justify-end gap-4">
        <button onClick={handleDownloadMD} className="btn-secondary flex items-center gap-2 text-sm py-2"><FileText size={16} /> Markdown</button>
        <button onClick={handleDownloadJSON} className="btn-secondary flex items-center gap-2 text-sm py-2"><FileJson size={16} /> JSON</button>
        <button onClick={handleDownloadPDF} className="btn-primary flex items-center gap-2 text-sm py-2"><Download size={16} /> Download PDF</button>
      </div>

      {/* 1. Summary Card */}
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="glass-panel p-8 text-center">
        <div className={`w-24 h-24 mx-auto rounded-full flex items-center justify-center mb-6 ${isRisky ? 'bg-danger/20 text-danger' : 'bg-success/20 text-success'}`}>
          {isRisky ? <ShieldAlert size={48} /> : <ShieldCheck size={48} />}
        </div>
        <h1 className="text-4xl font-bold mb-2">{data.risk_score} / 100</h1>
        <div className={`text-xl font-medium mb-4 ${isRisky ? 'text-danger' : 'text-success'}`}>{data.risk_level} Risk</div>
        <p className="text-gray-400 font-mono">{data.target}</p>
      </motion.div>

      {/* 2. AI Recommendations */}
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }}>
        <h2 className="text-2xl font-bold mb-4 flex items-center gap-2">
          <ArrowRight className="text-primary" /> AI Recommendations
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {data.recommendations?.map((rec: string, i: number) => (
            <div key={i} className={`p-4 rounded-xl border ${isRisky ? 'bg-danger/5 border-danger/20' : 'bg-surface border-border'} font-medium`}>
              {rec}
            </div>
          ))}
          {data.official_url && (
            <a href={data.official_url} target="_blank" rel="noreferrer" className="p-4 rounded-xl border bg-primary/10 border-primary/30 text-primary font-medium hover:bg-primary/20 transition">
              Visit Official Site: {data.official_url}
            </a>
          )}
        </div>
      </motion.div>

      {/* 3. Why Section */}
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.2 }} className="glass-panel p-8">
        <h2 className="text-2xl font-bold mb-6">Why is this website {isRisky ? 'risky' : 'safe'}?</h2>
        <ul className="space-y-4">
          {whyExplanations.map((exp: string, i: number) => (
            <li key={i} className="flex items-start gap-3 text-gray-300">
              <AlertTriangle className={`shrink-0 mt-1 ${isRisky ? 'text-danger' : 'text-success'}`} size={20} />
              <span className="leading-relaxed">{exp}</span>
            </li>
          ))}
        </ul>
      </motion.div>

      {/* 4. Cyber Tip Card */}
      <motion.div initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} transition={{ delay: 0.4 }} className="bg-gradient-to-r from-primary/20 to-blue-500/20 border border-primary/30 rounded-xl p-6 flex items-center gap-4">
        <div className="bg-primary/20 p-3 rounded-full text-primary">
          <Lightbulb size={24} />
        </div>
        <div>
          <h4 className="font-bold text-white mb-1">Cyber Safety Tip</h4>
          <p className="text-gray-300 text-sm">Always verify the URL before entering your password. Scammers often use convincing lookalikes.</p>
        </div>
      </motion.div>
    </div>
  );
};

export default Results;
