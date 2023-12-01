#!/usr/bin/env elixir
defmodule Main do
  def main do
    IO.read(:stdio, :all)
    |> String.split("\n")
    |> Stream.map(&String.replace(&1, ~R"[^0-9]", ""))
    |> Stream.filter(&(String.length(&1) > 0))
    |> Stream.map(&(String.first(&1) <> String.last(&1)))
    |> Stream.map(&String.to_integer/1)
    |> Enum.sum()
    |> IO.puts()
  end
end

Main.main()
