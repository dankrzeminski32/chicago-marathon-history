import { useEffect, useState } from "react";
import { Chart, registerables } from "chart.js";
import { Pie } from "react-chartjs-2";
import axios from "axios";

export const CountryDistribution = ({ marathon }) => {
    const [chartData, SetChartData] = useState({});
    const [chartOptions, SetChartOptions] = useState({});
    const [haveData, setHaveData] = useState(false);

    Chart.register(...registerables);

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:5000/api/results/" + marathon.year + "/M",
        }).then((response) => {
            const labels = [...new Set(response.data.map((item) => {}))];
            SetChartData({
                labels: labels,
                datasets: [
                    {
                        data: [
                            marathon.num_athletes_male,
                            marathon.num_athletes_female,
                        ],
                        backgroundColor: ["skyblue", "pink"],
                    },
                ],
            });
            setHaveData(true);
        });
    }, [marathon]);

    useEffect(() => {
        SetChartOptions({
            responsive: true,
            plugins: {
                legend: { display: false },
                title: {
                    display: true,
                    text:
                        "Athlete Distribution --- " +
                        marathon.num_athletes +
                        " Total Athletes",
                },
            },
        });
        setHaveData(true);
    }, [marathon]);

    if (!haveData) {
        // here
        return <div>Loading...</div>;
    }
    return (
        <div>
            <Bar options={chartOptions} data={chartData} />
        </div>
    );
};
