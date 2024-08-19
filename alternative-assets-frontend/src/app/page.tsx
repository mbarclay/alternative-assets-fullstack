import styles from "./page.module.css";
import InvestorsTable from "@/app/components/InvestorsTable";

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.div}>
        <h2 className={styles.h2}>Investors</h2>
      </div>
        <div className={styles.div}>
            <InvestorsTable/>
        </div>
    </main>
  );
}