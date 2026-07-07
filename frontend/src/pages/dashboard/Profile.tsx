import React from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';

export const Profile = () => {
  return (
    <div className="space-y-8 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold">User Profile</h1>
      <Card className="p-6">
        <div className="flex items-center gap-6 mb-8">
          <div className="h-24 w-24 rounded-full bg-gradient-to-tr from-primary to-purple-500 flex items-center justify-center text-4xl text-white font-bold">
            A
          </div>
          <div>
            <h2 className="text-2xl font-bold">Admin User</h2>
            <p className="text-text-muted">admin@trustguard.ai</p>
            <Badge className="mt-2" variant="success">Pro Plan</Badge>
          </div>
        </div>
        
        <form className="space-y-4 max-w-md">
          <div>
            <label className="block text-sm font-medium mb-1">Full Name</label>
            <input type="text" className="w-full bg-background border border-white/10 rounded-lg px-4 py-2" defaultValue="Admin User" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Email</label>
            <input type="email" className="w-full bg-background border border-white/10 rounded-lg px-4 py-2" defaultValue="admin@trustguard.ai" />
          </div>
          <Button className="mt-4">Save Changes</Button>
        </form>
      </Card>
    </div>
  );
};

// Dummy Badge component for profile
const Badge = ({ children, variant, className }: any) => (
  <span className={`px-2 py-1 text-xs font-semibold rounded-full bg-secondary/20 text-secondary ${className}`}>{children}</span>
);
