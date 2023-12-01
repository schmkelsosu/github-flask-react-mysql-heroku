import { useState, useEffect } from "react";

export default function BackendTest() {

    const [apiResponse, setApiResponse] = useState({});

    useEffect(() => {
        const getApiResponse = async () => {
            const response = await fetch("/api");
            const responseJson = await response.json();
            if (responseJson) {
                setApiResponse(responseJson);
            }
        };
        
        getApiResponse()
            .catch(console.error);
    }, []);

    return (
        <h1>{apiResponse.backendtest}</h1>
    )
}