import Head from 'next/head'
import dynamic from 'next/dynamic'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

const ReactAdmin = dynamic(() => import("../components/ReactAdmin"), { ssr: false });

export default function AdminPage() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Admin</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <ReactAdmin/>
    </div>
  )
}
