import React, { useEffect, useState } from 'react';
import { Search, Filter, Trash2, ArrowRight } from 'lucide-react';
import api from '../utils/axios';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';

const History = () => {
  const [history, setHistory] = useState<any[]>([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const res = await api.get('/analytics/history');
        setHistory(res.data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchHistory();
  }, []);

  const filtered = history.filter(s => s.target.toLowerCase().includes(searchTerm.toLowerCase()));

  return (
    <div className="space-y-8">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <h1 className="text-3xl font-bold">Scan History</h1>
        <div className="flex gap-4 w-full md:w-auto">
          <div className="relative flex-1 md:w-64">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500 w-4 h-4" />
            <input 
              type="text" placeholder="Search domains..." 
              className="w-full bg-surface border border-border rounded-lg pl-10 pr-4 py-2 text-sm focus:outline-none focus:border-primary"
              value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>
          <button className="btn-secondary px-4 py-2 flex items-center gap-2 text-sm"><Filter size={16}/> Filters</button>
        </div>
      </div>

      <div className="glass-panel overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="border-b border-border bg-surface/50">
                <th className="p-4 font-medium text-gray-400">Target</th>
                <th className="p-4 font-medium text-gray-400">Type</th>
                <th className="p-4 font-medium text-gray-400">Risk Score</th>
                <th className="p-4 font-medium text-gray-400">Level</th>
                <th className="p-4 font-medium text-gray-400">Date</th>
                <th className="p-4 font-medium text-gray-400 text-right">Actions</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((scan, i) => (
                <motion.tr 
                  initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: i * 0.05 }}
                  key={scan.id} className="border-b border-border/50 hover:bg-surface/50 transition"
                >
                  <td className="p-4 font-mono text-sm">{scan.target}</td>
                  <td className="p-4 text-gray-400">{scan.scan_type}</td>
                  <td className="p-4 font-bold">{scan.risk_score}</td>
                  <td className="p-4">
                    <span className={`px-2 py-1 rounded text-xs font-bold ${
                      scan.risk_level === 'Critical' ? 'bg-danger/20 text-danger' : 
                      scan.risk_level === 'High' ? 'bg-orange-500/20 text-orange-500' : 'bg-success/20 text-success'
                    }`}>
                      {scan.risk_level}
                    </span>
                  </td>
                  <td className="p-4 text-gray-400 text-sm">{scan.date.split(' ')[0]}</td>
                  <td className="p-4 flex justify-end gap-3">
                    <Link to={`/app/results/${scan.id}`} className="text-primary hover:text-primary-light transition flex items-center gap-1 text-sm">
                      View <ArrowRight size={14} />
                    </Link>
                  </td>
                </motion.tr>
              ))}
              {filtered.length === 0 && (
                <tr><td colSpan={6} className="p-8 text-center text-gray-500">No scans found.</td></tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default History;
