import { useEffect, useState } from "react";
import React from "react";
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";
import axios from "axios";

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

export const AthleteGrowthByYear = () => {
    const [marathons, setMarathons] = useState([]);
    const [labels, setLabels] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:5000/api/marathons/",
        })
            .then((response) => {
                setMarathons(response.data.reverse());
                setError(null);
                setLabels(response.data.map((x) => x.year));
            })
            .catch(setError);
    }, []);

    const data = {
        labels,
        datasets: [
            {
                label: "Total Female Participants",
                data: marathons.map((x) => x.num_athletes_female),
                borderColor: "rgb(255, 99, 132)",
                backgroundColor: "rgba(255, 99, 132, 0.5)",
            },
            {
                label: "Total Male Participants",
                data: marathons.map((x) => x.num_athletes_male),
                borderColor: "rgb(53, 162, 235)",
                backgroundColor: "rgba(53, 162, 235, 0.5)",
            },
        ],
    };

    const options = {
        responsive: true,
        plugins: {
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "Decades of Growth",
            },
        },
    };
    if (error) return <p>an error occured</p>;
    return (
        <div>
            <Line options={options} data={data} />
        </div>
    );
};
