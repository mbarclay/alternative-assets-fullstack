'use client';

import styles from '@/app/page.module.css';
import { useState, useEffect } from 'react';
import { AssetSummary } from '@/app/model/AssetSummary';

interface AssetSummariesProps {
    onAssetSummarySelect: (name: string) => void;
    investorCode: string | undefined;
}

const AssetSummaryGrid = ({ onAssetSummarySelect, investorCode }: AssetSummariesProps) => {

    const [assetSummaries, setAssetSummaries] = useState<AssetSummary[]>([]);
    const [selectedAssetClassCode, setSelectedAssetClassCode] = useState<string | null>(null);

    useEffect(() => {
        fetch(`http://localhost:8000/assets-summary/${investorCode}`)
            .then((response) => response.json())
            .then((data) => setAssetSummaries(data))
            .catch((error) => console.error('Error fetching asset summaries for investor:', error));
    }, [investorCode]);

    return (
        <div>
            <ul>
                {assetSummaries.map((assetSummary) => (
                    <li key={assetSummary.asset_class_code} onClick={() => onAssetSummarySelect(assetSummary.asset_class)}>
                        {assetSummary.asset_class} ({assetSummary.total_commitment_amount})
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default AssetSummaryGrid;