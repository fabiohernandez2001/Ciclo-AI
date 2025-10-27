export async function fetchChampion({signal}) {
    let url = "http://localhost:8000/api/champions/"

    
    const response = await fetch(url, {signal})
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
    }
    const { champions } = await response.json();
    return champions

}