"use client";

import { FileText, Upload, CheckCircle, ArrowRight, Shield, Zap, Users } from "lucide-react";
import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-slate-900 to-slate-800">
      {/* Header */}
      <header className="container mx-auto px-6 py-4">
        <nav className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <FileText className="h-8 w-8 text-emerald-400" />
            <span className="text-xl font-bold text-white">TaxReady</span>
          </div>
          <div className="flex items-center gap-6">
            <Link href="/dashboard" className="text-slate-300 hover:text-white transition">
              Dashboard
            </Link>
            <Link 
              href="/upload" 
              className="bg-emerald-500 hover:bg-emerald-600 text-white px-4 py-2 rounded-lg transition"
            >
              Get Started
            </Link>
          </div>
        </nav>
      </header>

      {/* Hero */}
      <section className="container mx-auto px-6 py-20">
        <div className="max-w-3xl mx-auto text-center">
          <h1 className="text-5xl font-bold text-white mb-6">
            Your Tax Documents, <span className="text-emerald-400">Organized</span>
          </h1>
          <p className="text-xl text-slate-300 mb-8">
            Upload your Form 16, bank statements, mutual fund statements. 
            We extract the data, organize it, and give you a CA-ready report. 
            No more document hunting.
          </p>
          <div className="flex gap-4 justify-center">
            <Link 
              href="/upload" 
              className="bg-emerald-500 hover:bg-emerald-600 text-white px-8 py-3 rounded-lg text-lg font-semibold transition flex items-center gap-2"
            >
              Upload Documents <ArrowRight className="h-5 w-5" />
            </Link>
            <Link 
              href="/dashboard" 
              className="border border-slate-600 text-white px-8 py-3 rounded-lg text-lg font-semibold hover:bg-slate-700 transition"
            >
              View Demo
            </Link>
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="container mx-auto px-6 py-16">
        <h2 className="text-3xl font-bold text-white text-center mb-12">How It Works</h2>
        <div className="grid md:grid-cols-3 gap-8">
          <div className="bg-slate-800 rounded-xl p-6">
            <div className="h-12 w-12 bg-emerald-500/20 rounded-lg flex items-center justify-center mb-4">
              <Upload className="h-6 w-6 text-emerald-400" />
            </div>
            <h3 className="text-xl font-semibold text-white mb-2">1. Upload PDFs</h3>
            <p className="text-slate-400">
              Drag and drop your Form 16, bank statements, MF statements, AIS, 26AS. We support them all.
            </p>
          </div>
          <div className="bg-slate-800 rounded-xl p-6">
            <div className="h-12 w-12 bg-emerald-500/20 rounded-lg flex items-center justify-center mb-4">
              <Zap className="h-6 w-6 text-emerald-400" />
            </div>
            <h3 className="text-xl font-semibold text-white mb-2">2. We Extract</h3>
            <p className="text-slate-400">
              AI reads your documents, finds income, TDS, deductions, and organizes everything automatically.
            </p>
          </div>
          <div className="bg-slate-800 rounded-xl p-6">
            <div className="h-12 w-12 bg-emerald-500/20 rounded-lg flex items-center justify-center mb-4">
              <CheckCircle className="h-6 w-6 text-emerald-400" />
            </div>
            <h3 className="text-xl font-semibold text-white mb-2">3. CA Ready</h3>
            <p className="text-slate-400">
              Download a complete report. Hand it to your CA. ITR filing done in minutes, not hours.
            </p>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="container mx-auto px-6 py-16">
        <div className="grid md:grid-cols-3 gap-8">
          <div className="flex items-start gap-4">
            <Shield className="h-6 w-6 text-emerald-400 flex-shrink-0 mt-1" />
            <div>
              <h4 className="text-white font-semibold mb-1">100% Private</h4>
              <p className="text-slate-400 text-sm">Your data stays on your device. We don't store anything on external servers.</p>
            </div>
          </div>
          <div className="flex items-start gap-4">
            <Users className="h-6 w-6 text-emerald-400 flex-shrink-0 mt-1" />
            <div>
              <h4 className="text-white font-semibold mb-1">Beginner Friendly</h4>
              <p className="text-slate-400 text-sm">No tax knowledge needed. We explain everything in simple language.</p>
            </div>
          </div>
          <div className="flex items-start gap-4">
            <FileText className="h-6 w-6 text-emerald-400 flex-shrink-0 mt-1" />
            <div>
              <h4 className="text-white font-semibold mb-1">All Documents</h4>
              <p className="text-slate-400 text-sm">Form 16, AIS, 26AS, bank statements, MF statements, capital gains reports.</p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="container mx-auto px-6 py-16">
        <div className="bg-gradient-to-r from-emerald-600 to-emerald-500 rounded-2xl p-8 text-center">
          <h2 className="text-3xl font-bold text-white mb-4">Ready to simplify your ITR filing?</h2>
          <p className="text-emerald-100 mb-6">Free for up to 5 documents. No signup required.</p>
          <Link 
            href="/upload" 
            className="inline-block bg-white text-emerald-600 px-8 py-3 rounded-lg font-semibold hover:bg-emerald-50 transition"
          >
            Get Started Free
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-700 py-8">
        <div className="container mx-auto px-6 text-center text-slate-500">
          <p>Made with ❤️ for Indian taxpayers. © 2025 TaxReady</p>
        </div>
      </footer>
    </main>
  );
}