import {
  render,
  screen,
  cleanup,
  fireEvent,
  waitFor,
} from "@testing-library/react";
import renderer from "react-test-renderer";
import LoginForm from "../login/LoginForm";
import userEvent from "@testing-library/user-event";
import { Form } from "react-bootstrap";
import "@testing-library/jest-dom/extend-expect";

afterEach(() => {
  cleanup();
});

test("should render LoginForm component", () => {
  render(<LoginForm />);
  const loginformElement = screen.getByTestId("loginForm");
  expect(loginformElement).toBeInTheDocument();
});

test("should show text fields", () => {
  render(<LoginForm />);
  const textElement = screen.getByTestId("textfields");
  expect(textElement).toBeInTheDocument();
});

test("should show Go/login button", () => {
  render(<LoginForm />);
  const button = screen.getByTestId("goButton");
  expect(button).toBeInTheDocument();
});

test("selecting an option is working", () => {
  const { getByRole, getByText } = render(<LoginForm />);
  const controlElement = getByText("Customer");
  fireEvent.click(controlElement);
  fireEvent.click(getByText(controlElement.value));
  waitFor(() => expect(controlElement).toHaveTextContent(controlElement.value));
});

test("matches snapshot", () => {
  const tree = renderer.create(<LoginForm />);
  expect(tree).toMatchSnapshot();
});
