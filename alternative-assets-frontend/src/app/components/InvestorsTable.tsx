'use client';

import styles from '@/app/page.module.css'
import {useState, useEffect} from 'react';
import {Investor} from '../types/Investor'; // Adjust path based on your file structure

const InvestorsTable = () => {
    const [investors, setInvestors] = useState<Investor[]>([]);

    useEffect(() => {
        fetch('http://localhost:8000/investors')
            .then(response => response.json())
            .then(data => setInvestors(data))
            .catch(error => console.error('Error fetching investors:', error));
    }, []);

    const formatCurrency = (value: number): string => {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            notation: 'compact',
        }).format(value);
    };

    const formatDate = (epoch: number): string => {
        const date = new Date(epoch * 1000);
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
        });
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
                <tr key={investor.investor_code}>
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