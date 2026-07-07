import React from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';

export const Settings = () => {
  return (
    <div className="space-y-8 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold">Settings</h1>
      <Card className="p-6 space-y-6">
        <div>
          <h3 className="font-semibold text-lg mb-2">Appearance</h3>
          <div className="flex items-center gap-4">
            <Button variant="outline">Dark Mode (Default)</Button>
            <Button variant="outline">Light Mode</Button>
          </div>
        </div>
        <hr className="border-white/10" />
        <div>
          <h3 className="font-semibold text-lg mb-2">Notifications</h3>
          <div className="space-y-2">
            <label className="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" className="form-checkbox text-primary rounded" defaultChecked />
              <span>Email alerts for Critical threats</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" className="form-checkbox text-primary rounded" defaultChecked />
              <span>Weekly analytics digest</span>
            </label>
          </div>
        </div>
        <hr className="border-white/10" />
        <div>
          <h3 className="font-semibold text-lg mb-2">API Keys</h3>
          <p className="text-sm text-text-muted mb-4">Manage your personal API keys for programmatic access to the scanner.</p>
          <Button>Generate New Key</Button>
        </div>
      </Card>
    </div>
  );
};
