'use client';

import {useState} from 'react';
import styles from './page.module.css';
import InvestorsTable from '@/app/components/InvestorsTable';
import AssetSummaryGrid from "@/app/components/InvestorAssetSummaries";
import {Investor} from "@/app/model/Investor";
import InvestorCommitments from "@/app/components/InvestorCommitments";

export default function Home() {
    const [selectedInvestor, setSelectedInvestor] = useState<Investor | undefined>(undefined);
    const [selectedAssetCode, setSelectedAssetCode] = useState<string | undefined>(undefined);

    const handleInvestorSelect = (investor: Investor) => {
        setSelectedInvestor(investor);
        setSelectedAssetCode(undefined)
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
                <InvestorsTable onInvestorSelect={handleInvestorSelect}/>
            </div>
            <div className={styles.div}>
                <h2 className={styles.h2}>
                    Commitments: {selectedInvestor?.name ? selectedInvestor.name : '(choose investor)'}: {selectedAssetCode}
                </h2>
            </div>
            <div>
                <AssetSummaryGrid investorCode={selectedInvestor?.investor_code}
                                  onAssetSummarySelect={handleAssetSummarySelect}/>
            </div>
            <div>
                <InvestorCommitments investorCode={selectedInvestor?.investor_code} assetClassCode={selectedAssetCode}/>
            </div>
        </main>
    );
}