import { useEffect, useState } from "react";
import { Chart, registerables } from "chart.js";
import { Pie } from "react-chartjs-2";
import axios from "axios";

export const CountryDistribution = ({ marathon }) => {
    const [chartData, SetChartData] = useState({});
    const [haveData, setHaveData] = useState(false);

    Chart.register(...registerables);

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:5000/api/results/" + marathon.year,
        }).then((response) => {
            const labels = [
                ...new Set(response.data.map((item) => item.athlete.country)),
            ];
            console.log(labels);
            const count = labels.map((item) => {
                const countryCount = response.data.reduce(
                    (acc, cur) => (cur.athlete.country === item ? ++acc : acc),
                    0
                );
                return countryCount;
            });
            console.log(count);
            SetChartData({
                labels: labels,
                datasets: [
                    {
                        label: "Total Runners",
                        data: count,
                        backgroundColor: [
                            "rgba(255, 99, 132, 0.2)",
                            "rgba(54, 162, 235, 0.2)",
                            "rgba(255, 206, 86, 0.2)",
                            "rgba(75, 192, 192, 0.2)",
                            "rgba(153, 102, 255, 0.2)",
                            "rgba(255, 159, 64, 0.2)",
                        ],
                        borderColor: [
                            "rgba(255, 99, 132, 1)",
                            "rgba(54, 162, 235, 1)",
                            "rgba(255, 206, 86, 1)",
                            "rgba(75, 192, 192, 1)",
                            "rgba(153, 102, 255, 1)",
                            "rgba(255, 159, 64, 1)",
                        ],
                        borderWidth: 1,
                    },
                ],
            });
            setHaveData(true);
        });
    }, [marathon]);

    if (!haveData) {
        // here
        return <div>Loading...</div>;
    }
    return (
        <div>
            <Pie
                data={chartData}
                width={"300px"}
                height={"300px"}
                options={{
                    maintainAspectRatio: false,
                    responsive: false,
                    plugins: {
                        title: { display: true, text: "Country Distribution" },
                    },
                }}
            />
        </div>
    );
};
