import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { Upload, Camera, QrCode, ArrowRight } from 'lucide-react';
import { ScanWorkflow } from './ScanWorkflow';
import { useNavigate } from 'react-router-dom';

export const ScanQR = () => {
  const [isScanning, setIsScanning] = useState(false);
  const [activeTab, setActiveTab] = useState<'upload'|'camera'>('upload');
  const navigate = useNavigate();

  const handleScan = () => setIsScanning(true);
  const handleComplete = () => { setIsScanning(false); navigate('/app/results/2'); };

  return (
    <div className='max-w-4xl mx-auto space-y-8'>
      {isScanning && <ScanWorkflow onComplete={handleComplete} />}
      <h1 className='text-2xl font-bold'>Scan QR Code</h1>
      <Card className='p-8'>
        <div className='flex gap-4 mb-8 border-b border-white/10 pb-4'>
          <button onClick={() => setActiveTab('upload')} className={`pb-2 font-medium ${activeTab === 'upload' ? 'text-primary' : 'text-text-muted'}`}>Upload Image</button>
          <button onClick={() => setActiveTab('camera')} className={`pb-2 font-medium ${activeTab === 'camera' ? 'text-primary' : 'text-text-muted'}`}>Use Camera</button>
        </div>
        <Button onClick={handleScan}>Simulate Scan</Button>
      </Card>
    </div>
  );
};
