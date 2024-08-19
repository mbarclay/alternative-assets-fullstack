import styles from "./page.module.css";
import InvestorsTable from "@/app/components/InvestorsTable";

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.description}>
        <h2>Investors</h2>
      </div>
      {/*<div className={styles.tableWrapper}>*/}
        <InvestorsTable />
      {/*</div>*/}
    </main>
  );
}