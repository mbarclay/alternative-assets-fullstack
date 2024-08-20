import { formatCurrency, formatDate } from '../Formatters';

describe('formatCurrency', () => {
  it('should format a number as GBP currency with compact notation', () => {
    expect(formatCurrency(1000)).toBe('£1K');
    expect(formatCurrency(1500000)).toBe('£1.5M');
    expect(formatCurrency(2500000000)).toBe('£2.5B');
  });

  it('should handle small amounts correctly', () => {
    expect(formatCurrency(5)).toBe('£5');
    expect(formatCurrency(50)).toBe('£50');
    expect(formatCurrency(999)).toBe('£999');
  });

  it('should handle zero value correctly', () => {
    expect(formatCurrency(0)).toBe('£0');
  });

  it('should handle negative values correctly', () => {
    expect(formatCurrency(-1000)).toBe('-£1K');
    expect(formatCurrency(-250000)).toBe('-£250K');
    expect(formatCurrency(-9999999)).toBe('-£10M');
  });
});

describe('formatDate', () => {
  it('should format an epoch time to a readable date string in en-GB format', () => {
    expect(formatDate(1625247600)).toBe('2 July 2021');
    expect(formatDate(1609459200)).toBe('1 January 2021');
  });

  it('should handle epoch time for dates in the past', () => {
    expect(formatDate(0)).toBe('1 January 1970');
    expect(formatDate(946684800)).toBe('1 January 2000');
  });

  it('should handle epoch time for future dates', () => {
    const futureEpoch = new Date('2050-01-01').getTime() / 1000;
    expect(formatDate(futureEpoch)).toBe('1 January 2050');
  });
});