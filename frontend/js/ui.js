function Header() {
  return React.createElement(
    "div",
    { className: "header" },
    React.createElement("h1", null, "✨ LexiCorrect"),
    React.createElement(
      "p",
      { className: "subtitle" },
      "LexiCorrect is a lightweight natural language processing project that automatically corrects French sentences using statistical language models.",
    ),
  );
}

function TextArea({ value, onChange }) {
  return React.createElement("textarea", {
    value,
    onChange,
    placeholder: "Paste or type your text here for correction.",
  });
}

function Button({ label, onClick, disabled, className }) {
  return React.createElement("button", { onClick, disabled, className }, label);
}
