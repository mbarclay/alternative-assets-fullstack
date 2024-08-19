'use client';

import styles from '@/app/page.module.css';
import { useState, useEffect } from 'react';
import { InvestorCommitment } from '@/app/model/InvestorCommitment';
import { formatCurrency } from "@/app/utilities/Currency";

interface InvestorCommitmentsTableProps {
  investorCode: string | undefined;
  assetClassCode: string | undefined;
}

const InvestorCommitmentsTable = ({ investorCode, assetClassCode }: InvestorCommitmentsTableProps) => {
  const [commitments, setCommitments] = useState<InvestorCommitment[]>([]);

  useEffect(() => {
    const url = `http://localhost:8080/investor/${investorCode}/commitments/asset-class/${assetClassCode}`;

    fetch(url)
      .then((response) => response.json())
      .then((data) => setCommitments(data))
      .catch((error) => console.error('Error fetching commitments:', error));
  }, [investorCode, assetClassCode]);

  return (
    <table className={styles.table}>
      <thead>
        <tr>
          <th>UUID</th>
          <th>Asset Class Code</th>
          <th>Asset Class</th>
          <th>Currency</th>
          <th>Amount</th>
        </tr>
      </thead>
      <tbody>
        {commitments.map((commitment) => (
          <tr key={commitment.commitment_uuid}>
            <td>{commitment.commitment_uuid}</td>
            <td>{commitment.asset_class_code}</td>
            <td>{commitment.asset_class}</td>
            <td>{commitment.currency_code}</td>
            <td>{formatCurrency(commitment.amount)}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default InvestorCommitmentsTable;