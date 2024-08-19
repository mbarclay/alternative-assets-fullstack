'use client';

import {useState} from 'react';
import styles from './page.module.css';
import InvestorsTable from '@/app/components/InvestorsTable';
import AssetSummaryGrid from "@/app/components/InvestorAssetSummaries";
import {Investor} from "@/app/model/Investor";
import InvestorCommitments from "@/app/components/InvestorCommitments";
import {AssetSummary} from "@/app/model/AssetSummary";

export default function Home() {
    const [selectedInvestor, setSelectedInvestor] = useState<Investor | undefined>(undefined);
    const [selectedAssetSummary, setSelectedAssetSummary] = useState<AssetSummary | undefined>(undefined);

    const handleInvestorSelect = (investor: Investor) => {
        setSelectedInvestor(investor);
        setSelectedAssetSummary(undefined)
    };

    const handleAssetSummarySelect = (assetSummary: AssetSummary) => {
        setSelectedAssetSummary(assetSummary)
    }

    return (
        <main className={styles.main}>
            <div className={styles.div}>
                <h2 className={styles.h2}>Investors</h2>
            </div>
            <div className={styles.div}>
                <InvestorsTable onInvestorSelect={handleInvestorSelect}/>
            </div>

            { selectedInvestor && (
            <div className={styles.div}>
                <h2 className={styles.h2}>
                    Commitments: {selectedInvestor?.name ? selectedInvestor.name : ''}: {selectedAssetSummary?.asset_class}
                </h2>
            </div>
            )}
            
            { selectedInvestor && (
                <div>
                    <AssetSummaryGrid investorCode={selectedInvestor?.investor_code}
                                      onAssetSummarySelect={handleAssetSummarySelect}/>
                </div>
            )}

            {selectedAssetSummary && (
                <div>
                    <InvestorCommitments investorCode={selectedInvestor?.investor_code}
                                         assetClassCode={selectedAssetSummary?.asset_class_code}/>
                </div>
            )}
        </main>
    );
}