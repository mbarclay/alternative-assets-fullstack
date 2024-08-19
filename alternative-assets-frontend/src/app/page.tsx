'use client';

import { useState } from 'react';
import styles from './page.module.css';
import InvestorsTable from '@/app/components/InvestorsTable';
import AssetSummaryGrid from "@/app/components/InvestorAssetSummaries";
import {Investor} from "@/app/model/Investor";

export default function Home() {
  const [selectedInvestor, setSelectedInvestor] = useState<Investor | null>(null);
  const [selectedAssetCode, setSelectedAssetCode] = useState<string | null>(null);

  const handleInvestorSelect = (investor: Investor) => {
    setSelectedInvestor(investor);
    setSelectedAssetCode(null)
  };

  const handleAssetSummarySelect = (assetCode: string) => {
      setSelectedAssetCode(assetCode)
  }

  return (
    <main className={styles.main}>
      <div className={styles.div}>
        <h2 className={styles.h2}>Investors</h2>
      </div>
      <div className={styles.div}>
        <InvestorsTable onInvestorSelect={handleInvestorSelect} />
      </div>
      <div className={styles.div}>
        <h2 className={styles.h2}>
          Commitments: {selectedInvestor?.name ? selectedInvestor.name : ''}
        </h2>
      </div>
        <div>
            <AssetSummaryGrid investorCode={selectedInvestor?.investor_code} onAssetSummarySelect={handleAssetSummarySelect}/>
        </div>
    </main>
  );
}