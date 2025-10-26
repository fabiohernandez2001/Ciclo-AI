import { useEffect, useState } from "react"
/*
    Custom hook that returns a debounced value.
    The value will only update after the specified delay
    has passed without the value changing.
*/

export default function useDebounceValue(value, delay = 300) {
    const [debounce, setDebounce] = useState(value)
    useEffect(() => {
        const id = setTimeout(() => setDebounce(value), delay)
        return () => clearTimeout(id)
    }, [value, delay])
    return debounce
}