import React from 'react';
import { motion } from 'framer-motion';
import { Moon, Bell, Shield, Lock } from 'lucide-react';

const Settings = () => {
  return (
    <div className="max-w-4xl space-y-8">
      <div>
        <h1 className="text-3xl font-bold mb-2">Settings</h1>
        <p className="text-gray-400">Manage your preferences and workspace configurations.</p>
      </div>

      <motion.div 
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass-panel divide-y divide-border"
      >
        {/* Section 1 */}
        <div className="p-8 flex flex-col sm:flex-row sm:items-center justify-between gap-6">
          <div className="flex gap-4">
            <div className="w-10 h-10 rounded-full bg-surface flex items-center justify-center shrink-0">
              <Moon size={20} className="text-gray-300" />
            </div>
            <div>
              <h3 className="font-bold mb-1">Appearance</h3>
              <p className="text-sm text-gray-400">Customize the UI theme. Currently locked to Dark Mode for premium aesthetics.</p>
            </div>
          </div>
          <div className="flex bg-surface p-1 rounded-lg border border-border shrink-0">
            <button className="px-4 py-1.5 text-sm font-medium rounded-md text-gray-400 hover:text-white transition">Light</button>
            <button className="px-4 py-1.5 text-sm font-medium rounded-md bg-white/10 text-white shadow transition">Dark</button>
          </div>
        </div>

        {/* Section 2 */}
        <div className="p-8 flex flex-col sm:flex-row sm:items-center justify-between gap-6">
          <div className="flex gap-4">
            <div className="w-10 h-10 rounded-full bg-surface flex items-center justify-center shrink-0">
              <Bell size={20} className="text-gray-300" />
            </div>
            <div>
              <h3 className="font-bold mb-1">Notifications</h3>
              <p className="text-sm text-gray-400">Receive alerts when a scan detects a high-risk payload.</p>
            </div>
          </div>
          <label className="relative inline-flex items-center cursor-pointer shrink-0">
            <input type="checkbox" className="sr-only peer" defaultChecked />
            <div className="w-11 h-6 bg-surface peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-gray-300 after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
          </label>
        </div>

        {/* Section 3 */}
        <div className="p-8 flex flex-col sm:flex-row sm:items-center justify-between gap-6">
          <div className="flex gap-4">
            <div className="w-10 h-10 rounded-full bg-surface flex items-center justify-center shrink-0">
              <Shield size={20} className="text-gray-300" />
            </div>
            <div>
              <h3 className="font-bold mb-1">Aggressive Scanning</h3>
              <p className="text-sm text-gray-400">Enable advanced heuristics. May increase scan duration.</p>
            </div>
          </div>
          <label className="relative inline-flex items-center cursor-pointer shrink-0">
            <input type="checkbox" className="sr-only peer" />
            <div className="w-11 h-6 bg-surface peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-gray-300 after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
          </label>
        </div>
      </motion.div>
    </div>
  );
};

export default Settings;
