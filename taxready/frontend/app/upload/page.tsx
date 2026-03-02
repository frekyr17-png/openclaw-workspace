"use client";

import { useState, useCallback } from "react";
import { Upload, FileText, CheckCircle, XCircle, Loader2 } from "lucide-react";
import Link from "next/link";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

interface Document {
  id: string;
  filename: string;
  doc_type: string;
  status: string;
  created_at: string;
}

export default function UploadPage() {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [uploading, setUploading] = useState(false);
  const [dragActive, setDragActive] = useState(false);

  const handleDrag = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  }, []);

  const uploadFiles = async (files: FileList) => {
    setUploading(true);
    
    for (const file of Array.from(files)) {
      if (!file.name.toLowerCase().endsWith(".pdf")) {
        continue;
      }

      const formData = new FormData();
      formData.append("file", file);

      try {
        const res = await fetch(`${API_URL}/upload`, {
          method: "POST",
          body: formData,
        });
        
        if (res.ok) {
          const doc = await res.json();
          setDocuments((prev) => [doc, ...prev]);
        }
      } catch (err) {
        console.error("Upload error:", err);
      }
    }
    
    setUploading(false);
  };

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    
    if (e.dataTransfer.files) {
      uploadFiles(e.dataTransfer.files);
    }
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      uploadFiles(e.target.files);
    }
  };

  const docTypeLabels: Record<string, string> = {
    form16: "Form 16",
    bank_statement: "Bank Statement",
    mf_statement: "MF Statement",
    ais: "Annual Info Statement",
    form26as: "Form 26AS",
    capital_gains: "Capital Gains",
    credit_card: "Credit Card Statement",
    unknown: "Processing...",
  };

  const statusIcons: Record<string, React.ReactNode> = {
    pending: <Loader2 className="h-4 w-4 animate-spin text-yellow-400" />,
    processing: <Loader2 className="h-4 w-4 animate-spin text-blue-400" />,
    done: <CheckCircle className="h-4 w-4 text-emerald-400" />,
    error: <XCircle className="h-4 w-4 text-red-400" />,
  };

  return (
    <main className="min-h-screen bg-gradient-to-b from-slate-900 to-slate-800">
      {/* Header */}
      <header className="container mx-auto px-6 py-4">
        <nav className="flex items-center justify-between">
          <Link href="/" className="flex items-center gap-2">
            <FileText className="h-8 w-8 text-emerald-400" />
            <span className="text-xl font-bold text-white">TaxReady</span>
          </Link>
          <Link 
            href="/dashboard" 
            className="bg-emerald-500 hover:bg-emerald-600 text-white px-4 py-2 rounded-lg transition"
          >
            View Dashboard
          </Link>
        </nav>
      </header>

      {/* Upload Section */}
      <section className="container mx-auto px-6 py-16">
        <h1 className="text-3xl font-bold text-white text-center mb-2">
          Upload Your Documents
        </h1>
        <p className="text-slate-400 text-center mb-12">
          Drop your PDF files here. We support Form 16, bank statements, MF statements, AIS, 26AS, and more.
        </p>

        {/* Drop Zone */}
        <div
          className={`max-w-2xl mx-auto border-2 border-dashed rounded-xl p-12 text-center transition ${
            dragActive
              ? "border-emerald-400 bg-emerald-500/10"
              : "border-slate-600 hover:border-slate-500"
          }`}
          onDragEnter={handleDrag}
          onDragLeave={handleDrag}
          onDragOver={handleDrag}
          onDrop={handleDrop}
        >
          <Upload className="h-12 w-12 text-slate-500 mx-auto mb-4" />
          <p className="text-slate-300 mb-4">
            Drag & drop your PDF files here, or
          </p>
          <label className="cursor-pointer">
            <span className="bg-emerald-500 hover:bg-emerald-600 text-white px-6 py-2 rounded-lg transition inline-block">
              Browse Files
            </span>
            <input
              type="file"
              accept=".pdf"
              multiple
              className="hidden"
              onChange={handleChange}
              disabled={uploading}
            />
          </label>
          {uploading && (
            <p className="text-emerald-400 mt-4">
              <Loader2 className="h-4 w-4 animate-spin inline mr-2" />
              Uploading & processing...
            </p>
          )}
        </div>

        {/* Document List */}
        {documents.length > 0 && (
          <div className="max-w-2xl mx-auto mt-12">
            <h2 className="text-xl font-semibold text-white mb-4">
              Uploaded Documents ({documents.length})
            </h2>
            <div className="space-y-3">
              {documents.map((doc) => (
                <div
                  key={doc.id}
                  className="bg-slate-800 rounded-lg p-4 flex items-center justify-between"
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
                  <div className="flex items-center gap-2">
                    {statusIcons[doc.status]}
                    <span className="text-slate-400 text-sm capitalize">{doc.status}</span>
                  </div>
                </div>
              ))}
            </div>
            <Link
              href="/dashboard"
              className="block text-center mt-6 bg-emerald-500 hover:bg-emerald-600 text-white px-6 py-3 rounded-lg transition"
            >
              View Dashboard →
            </Link>
          </div>
        )}
      </section>
    </main>
  );
}