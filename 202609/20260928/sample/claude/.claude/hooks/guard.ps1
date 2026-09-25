param([switch]$Copilot)

$raw = [Console]::In.ReadToEnd()
try {
  $inputObject = $raw | ConvertFrom-Json -ErrorAction Stop
} catch {
  [Console]::Error.WriteLine("Invalid hook input: $_")
  exit 2
}

$command = $inputObject.tool_input.command
if (-not $command) {
  exit 0
}

if ($command -match 'git\s+push\b.*(\s-f\b|\s--force\b)') {
  if ($Copilot) {
    @{
      permissionDecision       = "deny"
      permissionDecisionReason = "force push is blocked by hook. Run it manually if really needed."
    } | ConvertTo-Json -Compress
  } else {
    @{
      hookSpecificOutput = @{
        hookEventName            = "PreToolUse"
        permissionDecision       = "deny"
        permissionDecisionReason = "force push is blocked by hook. Run it manually if really needed."
      }
    } | ConvertTo-Json -Compress -Depth 3
  }
}

exit 0
