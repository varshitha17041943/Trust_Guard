import React from 'react';
import { motion } from 'framer-motion';
import { User, Mail, Key } from 'lucide-react';

const Profile = () => {
  return (
    <div className="max-w-3xl mx-auto space-y-8">
      <h1 className="text-3xl font-bold">My Profile</h1>
      
      <motion.div 
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass-panel overflow-hidden"
      >
        <div className="bg-gradient-to-r from-primary/20 to-accent/20 h-32"></div>
        <div className="px-8 pb-8">
          <div className="-mt-12 mb-6 flex justify-between items-end">
            <div className="w-24 h-24 rounded-2xl bg-surface border-4 border-background flex items-center justify-center shadow-xl">
              <User size={40} className="text-gray-400" />
            </div>
            <button className="btn-secondary text-sm px-4 py-2">Edit Profile</button>
          </div>
          
          <div className="space-y-6">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div>
                <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Full Name</label>
                <div className="bg-surface px-4 py-3 rounded-lg border border-border text-white">Admin User</div>
              </div>
              <div>
                <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Email Address</label>
                <div className="bg-surface px-4 py-3 rounded-lg border border-border text-white flex items-center gap-2">
                  <Mail size={16} className="text-gray-400" /> admin@trustguard.ai
                </div>
              </div>
            </div>
            
            <div className="pt-6 border-t border-border">
              <h3 className="font-bold mb-4 flex items-center gap-2">
                <Key size={18} className="text-primary" /> Authentication
              </h3>
              <button className="btn-secondary text-sm">Change Password</button>
            </div>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default Profile;
