tailwind.config = {
  theme: {
    extend: {
      colors: {
        primary: "#3B82F6",
        darkbg: "#0B1120",
        cardbg: "#111827",
        success: "#10B981",
        danger: "#EF4444",
      },
      boxShadow: {
        glow: "0 0 20px rgba(59,130,246,0.5)",
        card: "0 20px 60px rgba(0,0,0,0.6)"
      },
      animation: {
        float: "float 4s ease-in-out infinite",
        fadeIn: "fadeIn 1s ease-in-out"
      },
      keyframes: {
        float: {
          "0%,100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-10px)" }
        },
        fadeIn: {
          "0%": { opacity: "0" },
          "100%": { opacity: "1" }
        }
      }
    }
  }
}