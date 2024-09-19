import { useState } from 'react';
import axios from 'axios';
import { Globe, FolderTree, Code, Server } from 'lucide-react';

const FuzzerForm = () => {
  const [url, setUrl] = useState('');
  const [domain, setDomain] = useState('');
  const [fuzzDirectory, setFuzzDirectory] = useState(false);
  const [fuzzSubdomain, setFuzzSubdomain] = useState(false);
  const [fuzzApi, setFuzzApi] = useState(false);
  const [fuzzVhost, setFuzzVhost] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState(null); // Add state to store fuzzing results
  const [errorMessage, setErrorMessage] = useState(null); // For any error messages

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    const actions = {
      fuzz_directory: fuzzDirectory,
      fuzz_subdomain: fuzzSubdomain,
      fuzz_api: fuzzApi,
      fuzz_vhost: fuzzVhost,
    };

    const data = {
      url,
      domain,
      actions
    };

    try {
      const response = await axios.post('http://localhost:5000/fuzz', data);
      setResults(response.data.results); // Set the fuzzing results from the backend
      console.log(response.data);
      alert('Fuzzing completed successfully!');
    } catch (error) {
      console.error("Error fuzzing:", error);
      setErrorMessage('Failed to complete fuzzing. Please try again.');
      alert('Failed to complete fuzzing. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8 relative">
      {isLoading && (
        <div className="fixed inset-0 bg-gray-900 bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded-lg shadow-xl text-center">
            <div className="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-blue-500 mx-auto mb-4"></div>
            <p className="text-gray-700 font-semibold">Fuzzing in progress...</p>
          </div>
        </div>
      )}
      <h1 className="text-3xl font-bold mb-8 text-center">Web Fuzzer Tool</h1>
      <form onSubmit={handleSubmit} className="bg-gray-800 p-6 rounded-lg shadow-lg">
        <div className="mb-4">
          <label className="block text-sm font-bold mb-2" htmlFor="url">URL:</label>
          <input
            type="text"
            id="url"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="w-full p-3 bg-gray-700 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-bold mb-2" htmlFor="domain">Domain (for subdomain fuzzing):</label>
          <input
            type="text"
            id="domain"
            value={domain}
            onChange={(e) => setDomain(e.target.value)}
            className="w-full p-3 bg-gray-700 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <div className="mb-4">
          <label className="flex items-center space-x-2 cursor-pointer">
            <input
              type="checkbox"
              checked={fuzzDirectory}
              onChange={() => setFuzzDirectory(!fuzzDirectory)}
              className="form-checkbox h-5 w-5 text-blue-500"
            />
            <FolderTree size={20} />
            <span>Fuzz Directory</span>
          </label>
        </div>
        <div className="mb-4">
          <label className="flex items-center space-x-2 cursor-pointer">
            <input
              type="checkbox"
              checked={fuzzSubdomain}
              onChange={() => setFuzzSubdomain(!fuzzSubdomain)}
              className="form-checkbox h-5 w-5 text-blue-500"
            />
            <Globe size={20} />
            <span>Fuzz Subdomain</span>
          </label>
        </div>
        <div className="mb-4">
          <label className="flex items-center space-x-2 cursor-pointer">
            <input
              type="checkbox"
              checked={fuzzApi}
              onChange={() => setFuzzApi(!fuzzApi)}
              className="form-checkbox h-5 w-5 text-blue-500"
            />
            <Code size={20} />
            <span>Fuzz API</span>
          </label>
        </div>
        <div className="mb-4">
          <label className="flex items-center space-x-2 cursor-pointer">
            <input
              type="checkbox"
              checked={fuzzVhost}
              onChange={() => setFuzzVhost(!fuzzVhost)}
              className="form-checkbox h-5 w-5 text-blue-500"
            />
            <Server size={20} />
            <span>Fuzz Virtual Host</span>
          </label>
        </div>
        <button
          type="submit"
          className="w-full bg-blue-500 text-white px-6 py-3 rounded-md hover:bg-blue-600 disabled:opacity-50"
          disabled={isLoading}
        >
          Start Fuzzing
        </button>
      </form>
      {/* Display results */}
 {results && (
  <div className="mt-8 bg-gray-800 p-6 rounded-lg shadow-lg">
    <h2 className="text-2xl font-bold mb-4">Fuzzing Results:</h2>
    <pre className="bg-gray-900 p-4 rounded-lg text-white overflow-auto">
      {JSON.stringify(results, null, 2)}
    </pre>
  </div>
)}

{/* Display error message if any */}
{errorMessage && (
  <div className="mt-8 bg-red-600 p-6 rounded-lg shadow-lg text-white">
    <p>{errorMessage}</p>
  </div>
)}
    </div>
  );
};
 

export default FuzzerForm;