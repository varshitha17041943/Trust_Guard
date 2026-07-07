import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { Shield, ArrowRight, CheckCircle, AlertTriangle, Info } from 'lucide-react';
import { ScanWorkflow } from './ScanWorkflow';
import { useNavigate } from 'react-router-dom';

export const ScanWebsite = () => {
  const [url, setUrl] = useState('');
  const [error, setError] = useState('');
  const [isScanning, setIsScanning] = useState(false);
  const navigate = useNavigate();

  const handleScan = () => {
    if (!url) {
      setError('Please enter a URL to scan.');
      return;
    }
    const urlPattern = /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/;
    if (!urlPattern.test(url)) {
      setError('Please enter a valid URL (e.g., https://example.com)');
      return;
    }
    setError('');
    setIsScanning(true);
  };

  const handleComplete = () => {
    setIsScanning(false);
    navigate('/dashboard/results/1');
  };

  return (
    <div className='max-w-6xl mx-auto space-y-8'>
      {isScanning && <ScanWorkflow onComplete={handleComplete} />}
      
      <div>
        <h1 className='text-2xl font-bold'>Scan Website</h1>
        <p className='text-text-muted mt-1'>Analyze any URL for phishing, malware, or scams.</p>
      </div>

      <div className='grid lg:grid-cols-3 gap-8'>
        {/* Left Section - Input */}
        <div className='lg:col-span-2 space-y-6'>
          <Card>
            <h2 className='text-lg font-semibold mb-4'>Enter URL to Analyze</h2>
            <div className='space-y-4'>
              <div>
                <input
                  type='text'
                  value={url}
                  onChange={(e) => { setUrl(e.target.value); setError(''); }}
                  placeholder='https://example.com'
                  className='w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-lg focus:outline-none focus:ring-2 focus:ring-primary'
                />
                {error && <p className='text-danger text-sm mt-2 flex items-center gap-1'><AlertTriangle size={14}/>{error}</p>}
              </div>
              <Button size='lg' className='w-full text-lg group' onClick={handleScan}>
                Analyze Website
                <ArrowRight className='ml-2 group-hover:translate-x-1 transition-transform' />
              </Button>
            </div>

            <div className='mt-8 pt-6 border-t border-white/10'>
              <h3 className='text-sm text-text-muted mb-3 uppercase tracking-wider font-semibold'>Quick Examples</h3>
              <div className='flex flex-wrap gap-2'>
                {['https://amazon.com', 'https://google.com', 'https://github.com', 'http://secure-login.bank-update.com'].map(ex => (
                  <button 
                    key={ex} 
                    onClick={() => setUrl(ex)}
                    className='text-sm bg-white/5 hover:bg-primary/20 border border-white/10 hover:border-primary/50 transition-colors rounded-full px-4 py-1.5'
                  >
                    {ex}
                  </button>
                ))}
              </div>
            </div>
          </Card>
        </div>

        {/* Right Section - Tips */}
        <div className='space-y-6'>
          <Card className='bg-primary/5 border-primary/20 relative overflow-hidden'>
            <Shield className='absolute -right-6 -bottom-6 h-32 w-32 text-primary/10' />
            <h3 className='font-semibold mb-2 flex items-center gap-2'>
              <Info className='text-primary h-5 w-5' /> Why Scan?
            </h3>
            <p className='text-sm text-text-muted mb-4'>
              Our multi-agent AI system checks URLs against threat databases, analyzes the domain age, checks SSL certificates, and looks for visual similarities to known brands.
            </p>
            <ul className='space-y-2 text-sm'>
              <li className='flex items-center gap-2'><CheckCircle size={16} className='text-secondary' /> Real-time threat Intel</li>
              <li className='flex items-center gap-2'><CheckCircle size={16} className='text-secondary' /> Typo-squatting detection</li>
              <li className='flex items-center gap-2'><CheckCircle size={16} className='text-secondary' /> Explainable AI Reports</li>
            </ul>
          </Card>
        </div>
      </div>
    </div>
  );
};
