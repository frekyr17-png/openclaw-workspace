"use client";

import { useState, useEffect } from "react";
import { FileText, TrendingUp, IndianRupee, AlertCircle, CheckCircle, Download, RefreshCw } from "lucide-react";
import Link from "next/link";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

interface Document {
  id: string;
  filename: string;
  doc_type: string;
  status: string;
  created_at: string;
}

interface DashboardData {
  total_income: number;
  total_tds: number;
  total_deductions: number;
  documents_processed: number;
  documents_pending: number;
  missing_docs: string[];
}

export default function DashboardPage() {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [dashboard, setDashboard] = useState<DashboardData | null>(null);
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    setLoading(true);
    try {
      const [docsRes, dashRes] = await Promise.all([
        fetch(`${API_URL}/documents`),
        fetch(`${API_URL}/dashboard`),
      ]);
      
      if (docsRes.ok) {
        setDocuments(await docsRes.json());
      }
      if (dashRes.ok) {
        setDashboard(await dashRes.json());
      }
    } catch (err) {
      console.error("Fetch error:", err);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
    // Poll every 5 seconds for updates
    const interval = setInterval(fetchData, 5000);
    return () => clearInterval(interval);
  }, []);

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat("en-IN", {
      style: "currency",
      currency: "INR",
      maximumFractionDigits: 0,
    }).format(amount);
  };

  const docTypeLabels: Record<string, string> = {
    form16: "Form 16",
    bank_statement: "Bank Statement",
    mf_statement: "MF Statement",
    ais: "Annual Info Statement",
    form26as: "Form 26AS",
    capital_gains: "Capital Gains",
    credit_card: "Credit Card",
    unknown: "Processing...",
  };

  const missingDocLabels: Record<string, string> = {
    form16: "Form 16 (from employer)",
    bank_statement: "Bank Statement",
    mf_statement: "Mutual Fund Statement (CAS)",
    ais: "Annual Information Statement",
  };

  if (loading && documents.length === 0) {
    return (
      <main className="min-h-screen bg-gradient-to-b from-slate-900 to-slate-800 flex items-center justify-center">
        <RefreshCw className="h-8 w-8 text-emerald-400 animate-spin" />
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gradient-to-b from-slate-900 to-slate-800">
      {/* Header */}
      <header className="container mx-auto px-6 py-4">
        <nav className="flex items-center justify-between">
          <Link href="/" className="flex items-center gap-2">
            <FileText className="h-8 w-8 text-emerald-400" />
            <span className="text-xl font-bold text-white">TaxReady</span>
          </Link>
          <div className="flex items-center gap-4">
            <Link
              href="/upload"
              className="border border-emerald-500 text-emerald-400 hover:bg-emerald-500/10 px-4 py-2 rounded-lg transition"
            >
              Upload More
            </Link>
            <button
              onClick={fetchData}
              className="text-slate-400 hover:text-white transition"
            >
              <RefreshCw className="h-5 w-5" />
            </button>
          </div>
        </nav>
      </header>

      <section className="container mx-auto px-6 py-8">
        <h1 className="text-3xl font-bold text-white mb-8">Your Tax Dashboard</h1>

        {/* Stats */}
        <div className="grid md:grid-cols-4 gap-4 mb-8">
          <div className="bg-slate-800 rounded-xl p-6">
            <div className="flex items-center justify-between mb-2">
              <span className="text-slate-400">Total Income</span>
              <TrendingUp className="h-5 w-5 text-emerald-400" />
            </div>
            <p className="text-2xl font-bold text-white">
              {formatCurrency(dashboard?.total_income || 0)}
            </p>
          </div>
          <div className="bg-slate-800 rounded-xl p-6">
            <div className="flex items-center justify-between mb-2">
              <span className="text-slate-400">TDS Deducted</span>
              <IndianRupee className="h-5 w-5 text-blue-400" />
            </div>
            <p className="text-2xl font-bold text-white">
              {formatCurrency(dashboard?.total_tds || 0)}
            </p>
          </div>
          <div className="bg-slate-800 rounded-xl p-6">
            <div className="flex items-center justify-between mb-2">
              <span className="text-slate-400">Deductions</span>
              <CheckCircle className="h-5 w-5 text-purple-400" />
            </div>
            <p className="text-2xl font-bold text-white">
              {formatCurrency(dashboard?.total_deductions || 0)}
            </p>
          </div>
          <div className="bg-slate-800 rounded-xl p-6">
            <div className="flex items-center justify-between mb-2">
              <span className="text-slate-400">Documents</span>
              <FileText className="h-5 w-5 text-yellow-400" />
            </div>
            <p className="text-2xl font-bold text-white">
              {dashboard?.documents_processed || 0} / {documents.length}
            </p>
          </div>
        </div>

        {/* Missing Documents */}
        {dashboard?.missing_docs && dashboard.missing_docs.length > 0 && (
          <div className="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-6 mb-8">
            <div className="flex items-center gap-2 mb-3">
              <AlertCircle className="h-5 w-5 text-yellow-400" />
              <h2 className="text-lg font-semibold text-white">Missing Documents</h2>
            </div>
            <ul className="space-y-2">
              {dashboard.missing_docs.map((doc) => (
                <li key={doc} className="text-slate-300">
                  • {missingDocLabels[doc] || doc}
                </li>
              ))}
            </ul>
            <Link
              href="/upload"
              className="inline-block mt-4 bg-yellow-500 hover:bg-yellow-600 text-black font-medium px-4 py-2 rounded-lg transition"
            >
              Upload Missing Documents
            </Link>
          </div>
        )}

        {/* Document List */}
        <div className="bg-slate-800 rounded-xl p-6">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-xl font-semibold text-white">Uploaded Documents</h2>
            {documents.length > 0 && (
              <button className="bg-emerald-500 hover:bg-emerald-600 text-white px-4 py-2 rounded-lg transition flex items-center gap-2">
                <Download className="h-4 w-4" />
                Export CA Report
              </button>
            )}
          </div>
          
          {documents.length === 0 ? (
            <div className="text-center py-12">
              <FileText className="h-12 w-12 text-slate-600 mx-auto mb-4" />
              <p className="text-slate-400 mb-4">No documents uploaded yet</p>
              <Link
                href="/upload"
                className="bg-emerald-500 hover:bg-emerald-600 text-white px-6 py-2 rounded-lg transition inline-block"
              >
                Upload Your First Document
              </Link>
            </div>
          ) : (
            <div className="space-y-3">
              {documents.map((doc) => (
                <div
                  key={doc.id}
                  className="bg-slate-700/50 rounded-lg p-4 flex items-center justify-between"
                >
                  <div className="flex items-center gap-3">
                    <FileText className="h-5 w-5 text-emerald-400" />
                    <div>
                      <p className="text-white font-medium">{doc.filename}</p>
                      <p className="text-slate-400 text-sm">
                        {docTypeLabels[doc.doc_type] || doc.doc_type}
                      </p>
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    <span
                      className={`px-3 py-1 rounded-full text-sm ${
                        doc.status === "done"
                          ? "bg-emerald-500/20 text-emerald-400"
                          : doc.status === "error"
                          ? "bg-red-500/20 text-red-400"
                          : "bg-yellow-500/20 text-yellow-400"
                      }`}
                    >
                      {doc.status}
                    </span>
                    <span className="text-slate-500 text-sm">
                      {new Date(doc.created_at).toLocaleDateString()}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </section>
    </main>
  );
}