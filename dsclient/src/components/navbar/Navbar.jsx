import { Link } from "react-router-dom";
import "./navbar.css";

export default function Navbar() {
    return (<header>
        <h3>Shop Digify</h3>
        <div>
            <Link to={'/'}>Home</Link>
            <Link to={'/about'}>About</Link>
        </div>
        <div>
            <Link to={'/'}>Sign up</Link>
            <Link to={'/about'}>Login</Link>
        </div>
    </header>)
}