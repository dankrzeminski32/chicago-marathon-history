import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function Sidebar({
    onHide,
    marathonStateChanger,
    isSidebarVisibleOnSmallScreen,
}) {
    const [marathons, setMarathons] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:5000/api/marathons/",
        })
            .then((response) => {
                setMarathons(response.data);
                setError(null);
            })
            .catch(setError);
    }, []);

    if (error) return <p>an error occured</p>;

    return (
        <div
            id="sidebar-wrapper"
            className={
                isSidebarVisibleOnSmallScreen
                    ? "d-md-block"
                    : "d-none d-md-block"
            }
        >
            <ul
                className={`sidebar-nav ${
                    isSidebarVisibleOnSmallScreen
                        ? "d-md-block"
                        : "d-none d-md-block"
                }`}
            >
                <li className="sidebar-brand">
                    <Link to="/">Years</Link>
                </li>
                {marathons.map((marathon) => {
                    return (
                        <li key={marathon.id} className="sidebar-brand">
                            <Link
                                onClick={() => {
                                    onHide();
                                    marathonStateChanger(marathon);
                                }}
                                to="/"
                            >
                                {marathon.year}
                            </Link>
                        </li>
                    );
                })}
            </ul>
        </div>
    );
}

export default Sidebar;
