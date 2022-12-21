import { useEffect, useState } from "react";
import React from "react";
import {
    Chart,
    LinearScale,
    PointElement,
    LineElement,
    Tooltip,
    Legend,
} from "chart.js";
import { Scatter } from "react-chartjs-2";
import axios from "axios";

export const LineFinishTimes = ({ marathon }) => {
    const [chartData, SetChartData] = useState({});
    const [haveData, setHaveData] = useState(false);
    const [athletes, setAthletes] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:5000/api/athletes/" + marathon.year,
        })
            .then((response) => {
                console.log("HERE" + response.data);
                setAthletes(response.data);
                setError(null);
            })
            .catch(setError);
    }, [marathon]);

    Chart.register(LinearScale, PointElement, LineElement, Tooltip, Legend);
    console.log(athletes);

    useEffect(() => {
        SetChartData({
            labels: "A dataset",
            datasets: [
                {
                    data: [
                        {
                            x: marathon.num_athletes_male,
                            y: marathon.num_athletes_female,
                        },
                    ],
                    backgroundColor: ["skyblue", "pink"],
                },
            ],
        });
        setHaveData(true);
    }, [marathon]);

    const options = {
        scales: {
            y: {
                beginAtZero: true,
            },
        },
    };

    if (!haveData) {
        // here
        return <div>Loading...</div>;
    }
    return (
        <div>
            <Scatter options={options} data={chartData} />
        </div>
    );
};
