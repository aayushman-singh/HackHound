import React from 'react';
import { Link } from 'react-scroll';

const Card = ({ icon, title, children }) => (
  <div className="bg-white bg-opacity-10 backdrop-filter backdrop-blur-lg border border-white border-opacity-20 rounded-xl p-6 flex flex-col items-center">
    {icon}
    <h3 className="text-2xl font-semibold mb-4 text-white">{title}</h3>
    <p className="text-gray-300 text-center">{children}</p>
  </div>
);

const GlassButton = ({ to, children }) => (
  <Link
    to={to}
    smooth={true}
    duration={500}
    className="mt-8 inline-block px-8 py-4 text-lg font-semibold bg-white bg-opacity-10 backdrop-filter backdrop-blur-lg border border-white border-opacity-20 rounded-full text-white hover:bg-opacity-20 transition-all"
  >
    {children}
  </Link>
);

// Custom Icon components
const ShieldIcon = () => (
  <svg className="w-16 h-16 mb-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20.618 5.984A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016zM12 9v2m0 4h.01" />
  </svg>
);

const SearchIcon = () => (
  <svg className="w-16 h-16 mb-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
  </svg>
);

const GlassCard = ({ title, children }) => (
  <div className="bg-white bg-opacity-10 backdrop-filter backdrop-blur-lg rounded-xl p-6 border border-white border-opacity-20">
    <h3 className="text-2xl font-semibold text-white mb-3">{title}</h3>
    <p className="text-lg text-gray-300">{children}</p>
  </div>
);

const TeamMember = ({ name, role, description, image }) => (
  <div className="bg-white bg-opacity-10 backdrop-filter backdrop-blur-lg rounded-xl p-4 border border-white border-opacity-20 text-center w-64"> {/* Fixed width for the card */}
    {/* Image Container */}
    <div className="relative w-[102.04px] h-[160px] mx-auto mb-4"> {/* Fixed dimensions for the image container */}
      <img
        src={image}
        alt={`${name}'s profile`}
        className="absolute top-0 left-0 w-full h-full object-cover rounded-sm"
      />
    </div>
    
    <h3 className="text-lg font-semibold text-white mb-1">{name}</h3> {/* Adjusted text size */}
    <p className="text-sm text-blue-400 mb-2">{role}</p> {/* Adjusted text size */}
    
    {/* Optional description */}
    <p className="text-xs text-white">{description}</p> {/* Adjusted text size */}
  </div>
);

const FileTextIcon = () => (
  <svg className="w-16 h-16 mb-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
  </svg>
);

const Home = () => {
  return (
    <div className="bg-gradient-to-br from-gray-900 to-blue-900 text-white min-h-screen">
      {/* Section 1: Home */}
      <section className="h-screen flex items-center justify-center px-4 relative overflow-hidden">
        <div className="absolute inset-0 bg-[url('/api/placeholder/1920/1080')] bg-cover bg-center opacity-10"></div>
        <div className="relative z-20 text-center">
          <h1 className="text-5xl sm:text-7xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-600 py-4">
            Welcome to HackHound
          </h1>
          <p className="text-xl sm:text-2xl text-gray-300 mt-4 max-w-3xl mx-auto">
            Enhancing Web Application Security: Comprehensive Fuzzing for Vulnerability Detection and Mitigation.
          </p>
          <GlassButton to="about">
            Learn More
          </GlassButton>
          <div className="text-center mt-8">
            <Link to ="/hack-hound/services"
              className="inline-block px-7 py-3 text-lg font-semibold bg-blue-600 bg-opacity-50 rounded-full hover:bg-opacity-75 transition-all"
            >
              Explore Services
            </Link>
          </div>
        </div>
      </section>

     {/* Section 2: About */}
<section id="about" className="min-h-screen flex flex-col justify-center items-center px-4 py-16 text-white relative overflow-hidden">
  <div className="absolute inset-0 bg-[url('/api/placeholder/1920/1080')] bg-cover bg-center opacity-10"></div>
  <div className="container mx-auto z-10">
    <h2 className="text-5xl font-bold mb-12 text-center">Who We Are</h2>
    <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
      <Card icon={<ShieldIcon />} title="Comprehensive Fuzzing">
        Our versatile web application fuzzer automates the discovery and testing of hidden directories, API endpoints, and virtual hosts to identify vulnerabilities before attackers can exploit them.
      </Card>
      <Card icon={<SearchIcon />} title="Deep Vulnerability Testing">
        We target URL parameters, subdomains, and other web components, performing comprehensive fuzzing to uncover security flaws like SQL injection, XSS, and directory traversal, ensuring enhanced protection of your web applications.
      </Card>
      <Card icon={<FileTextIcon />} title="Automated Security Reports">
        Our tool provides detailed reports on identified vulnerabilities, prioritizing them based on severity. It documents findings and recommends actionable remediation steps to help fortify your web applications.
      </Card>
    </div>
    <p className="text-lg text-gray-300 max-w-4xl mt-12 text-center mx-auto">
      Whether you're securing complex applications with custom components or targeting specific vulnerabilities, our fuzzer provides early detection and mitigation, enhancing both code quality and overall security.
    </p>
  </div>
</section>


     {/* Section 3: Services */}
<section id="services" className="min-h-screen w-full flex items-center justify-center relative py-20">
  <div className="absolute inset-0 bg-[url('/api/placeholder/1920/1080')] bg-cover bg-center opacity-10"></div>
  <div className="relative z-20 container mx-auto px-4">
    <h2 className="text-5xl sm:text-7xl font-bold text-center bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-600 mb-8">
      Our Services
    </h2>
    <p className="text-xl sm:text-2xl text-gray-300 mt-4 max-w-3xl mx-auto text-center mb-12">
      We provide comprehensive fuzzing services for web applications, covering directories, subdomains, API endpoints, and virtual hosts. Our tool automates the process, ensuring early detection of vulnerabilities to enhance your application's security.
    </p>
    <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
      <GlassCard title="Directory Fuzzing">
        Our tool performs systematic directory enumeration, helping identify hidden files and directories. This reveals potential vulnerabilities like directory traversal and exposed sensitive files.
      </GlassCard>
      <GlassCard title="Subdomain Fuzzing">
        Uncover subdomains linked to your application using brute-force and DNS enumeration techniques. We help identify additional attack surfaces and misconfigurations across your infrastructure.
      </GlassCard>
      <GlassCard title="API and Virtual Host Fuzzing">
        Detect and test API endpoints and virtual hosts for security flaws. We automate the fuzzing of APIs and virtual hosts to expose misconfigurations, authorization flaws, and potential injection points.
      </GlassCard>
    </div>
    <div className="text-center mt-12">
      <Link to="/services"
        className="inline-block px-8 py-4 text-lg font-semibold bg-blue-600 bg-opacity-50 rounded-full hover:bg-opacity-75 transition-all"
      >
        Explore Services
      </Link>
    </div>
  </div>
</section>
    </div>
  );
};

export default Home;
