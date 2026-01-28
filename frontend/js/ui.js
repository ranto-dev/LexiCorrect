function Header() {
  return React.createElement(
    "div",
    { className: "header" },
    React.createElement("h1", null, "✨ Correcteur IA 3D"),
    React.createElement(
      "p",
      { className: "subtitle" },
      "Propulsé par l'Intelligence Artificielle & Three.js",
    ),
  );
}

function TextArea({ value, onChange }) {
  return React.createElement("textarea", {
    value,
    onChange,
    placeholder: "Entrez votre texte ici...",
  });
}

function Button({ label, onClick, disabled, className }) {
  return React.createElement("button", { onClick, disabled, className }, label);
}
