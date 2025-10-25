import { useEffect } from "react";

/*
  Custom hook that alerts clicks outside of the passed ref element.
  Calls the handler function when a click is detected outside the element.
*/

export default function useOnClickOutside(ref, handler) {
  useEffect(() => {
    const listener = (event) => {
      const el = ref.current
      if (!el || el.contains(event.target)) return
      handler(event)
    }
    document.addEventListener("pointerdown", listener, true)
    return () => {
      document.removeEventListener("pointerdown", listener, true)
    }
  }, [ref, handler])
}