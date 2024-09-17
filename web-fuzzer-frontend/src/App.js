import React, { useState } from 'react';
import axios from 'axios';

const FuzzerForm = () => {
  const [url, setUrl] = useState('');
  const [domain, setDomain] = useState('');
  const [fuzzDirectory, setFuzzDirectory] = useState(false);
  const [fuzzSubdomain, setFuzzSubdomain] = useState(false);
  const [fuzzApi, setFuzzApi] = useState(false);
  const [fuzzVhost, setFuzzVhost] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
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
      console.log(response.data);
    } catch (error) {
      console.error("Error fuzzing:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>URL:</label>
        <input type="text" value={url} onChange={(e) => setUrl(e.target.value)} required />
      </div>
      <div>
        <label>Domain (for subdomain fuzzing):</label>
        <input type="text" value={domain} onChange={(e) => setDomain(e.target.value)} />
      </div>
      <div>
        <label>
          <input type="checkbox" checked={fuzzDirectory} onChange={() => setFuzzDirectory(!fuzzDirectory)} />
          Fuzz Directory
        </label>
      </div>
      <div>
        <label>
          <input type="checkbox" checked={fuzzSubdomain} onChange={() => setFuzzSubdomain(!fuzzSubdomain)} />
          Fuzz Subdomain
        </label>
      </div>
      <div>
        <label>
          <input type="checkbox" checked={fuzzApi} onChange={() => setFuzzApi(!fuzzApi)} />
          Fuzz API
        </label>
      </div>
      <div>
        <label>
          <input type="checkbox" checked={fuzzVhost} onChange={() => setFuzzVhost(!fuzzVhost)} />
          Fuzz Virtual Host
        </label>
      </div>
      <button type="submit">Start Fuzzing</button>
    </form>
  );
};

export default FuzzerForm;
