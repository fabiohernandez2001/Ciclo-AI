import { useEffect, useState } from "react"

export default function useDebounceValue(value, delay = 300) {
    const [debounce, setDebounce] = useState(value)
    useEffect(() => {
        const id = setTimeout(() => setDebounce(value), delay)
        return () => clearTimeout(id)
    }, [value, delay])
    return debounce
}