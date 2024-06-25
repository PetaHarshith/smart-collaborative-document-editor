import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
    return(
        <header className = "header">
            <div className = "header-content">
                <h1>Smart Collaborative Document Editing Platform</h1>
                <nav>
                    <ul className = "nav-links">
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/dashboard">Dashboard</Link></li>                       
                    </ul>
                </nav>
            </div>
        </header>
    );
};
