'use client';

import styles from '@/app/page.module.css';
import { useState, useEffect } from 'react';
import { Investor } from '@/app/model/Investor';
import { formatCurrency, formatDate } from '@/app/utilities/Formatters';

interface InvestorsTableProps {
  onInvestorSelect: (investor: Investor) => void;
}

const InvestorsTable = ({ onInvestorSelect }: InvestorsTableProps) => {
  const [investors, setInvestors] = useState<Investor[]>([]);
  const [selectedInvestor, setSelectedInvestor] = useState<
    Investor | undefined
  >(undefined);

  useEffect(() => {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL;
    const url = `${apiUrl}/investors`;

    fetch(url)
      .then((response) => response.json())
      .then((data) => setInvestors(data as Investor[]))
      .catch((error) => console.error('Error fetching investors:', error));
  }, []);

  const handleRowClick = (investor: Investor) => {
    setSelectedInvestor(investor);
    onInvestorSelect(investor);
  };

  return (
    <table className={styles.table}>
      <thead>
        <tr>
          <th>Code</th>
          <th>Name</th>
          <th>Type</th>
          <th>Date Added</th>
          <th>Country</th>
          <th>Total Commitment</th>
        </tr>
      </thead>
      <tbody>
        {investors.map((investor) => (
          <tr
            key={investor.investor_code}
            id={`investor-row-${investor.investor_code}`}
            className={
              selectedInvestor?.investor_code === investor.investor_code
                ? styles.selectedRow
                : ''
            }
            onClick={() => handleRowClick(investor)}
          >
            <td>{investor.investor_code}</td>
            <td>{investor.name}</td>
            <td>{investor.investory_type}</td>
            <td>{formatDate(investor.added_epoch)}</td>
            <td>{investor.country_name}</td>
            <td>{formatCurrency(investor.total_commitment)}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default InvestorsTable;
