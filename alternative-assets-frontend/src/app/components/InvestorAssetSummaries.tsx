'use client';

import styles from '@/app/page.module.css';
import { useState, useEffect } from 'react';
import { AssetSummary } from '@/app/model/AssetSummary';
import { formatCurrency } from '@/app/utilities/Formatters';

interface AssetSummariesProps {
  onAssetSummarySelect: (assetSummary: AssetSummary) => void;
  investorCode: string | undefined;
}

const AssetSummaryGrid = ({
  onAssetSummarySelect,
  investorCode,
}: AssetSummariesProps) => {
  const [assetSummaries, setAssetSummaries] = useState<AssetSummary[]>([]);

  useEffect(() => {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL;
    fetch(`${apiUrl}/assets-summary/${investorCode}`)
      .then((response) => response.json())
      .then((data) => setAssetSummaries(data as AssetSummary[]))
      .catch((error) =>
        console.error('Error fetching asset summaries for investor:', error),
      );
  }, [investorCode]);

  return (
    <div className={styles.gridContainer}>
      {assetSummaries.map((assetSummary) => (
        <div
          key={assetSummary.asset_class_code}
          id={`asset-summary-${assetSummary.asset_class_code}`}
          className={styles.card}
          onClick={() => onAssetSummarySelect(assetSummary)}
        >
          <h4>{assetSummary.asset_class}</h4>
          <p>{formatCurrency(assetSummary.total_commitment_amount)}</p>
        </div>
      ))}
    </div>
  );
};

export default AssetSummaryGrid;
