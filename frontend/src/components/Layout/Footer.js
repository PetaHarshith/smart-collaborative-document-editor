// footer contains:
// 1) info about creators: github acct, email id
// 2) support: links to drop question and report bugs
// 3) color scheme: light blue background, black text, dark blue links


import React from 'react';
import { Link } from 'react-router-dom';
import './footer.css';

const Footer = () => {
    return(
        <footer className = "footer">
            <div className = "footer-content">
                <h1>Creators</h1>
                <nav>
                    <ul className = "nav-links">
                    //add link to git
                        <li><Link to="/">Git</Link></li> 
                    //add links to email id
                        <li><Link to="/dashboard">email</Link></li>                       
                    </ul>
                </nav>
            </div>
        </footer>
    );
};
