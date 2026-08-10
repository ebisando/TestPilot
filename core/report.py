from pathlib import Path

class ReportGenerator:

    def generate(self, results):

        Path("reports").mkdir(
            exist_ok=True
        )

        template = open("templates/report_template.html", encoding="utf-8").read()
        total = len(results)

        passed = sum(
            1
            for result in results
            if result.status == "PASSED"
        )

        failed = total - passed

        summary = f"""
        <p><strong>Total Tests:</strong> {total}</p>
        <p><strong>Passed:</strong> {passed}</p>
        <p><strong>Failed:</strong> {failed}</p>
        """
        rows = ""

        for result in results:
            status_class = "pass" if result.status == "PASSED" else "fail"
            rows += f"<tr class='{status_class}'><td>{result.name}</td><td>{result.status}</td></tr>"

        report = template.replace("{{SUMMARY}}", summary).replace("{{ROWS}}", rows)
        with open("reports/index.html", "w", encoding="utf-8") as f:

            f.write(report)

          