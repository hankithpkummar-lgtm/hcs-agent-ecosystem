"""
AutoDesigner Pro - Demo Script
==============================
Demonstrates the full pipeline with a sample website.
"""
import asyncio
import os
import tempfile
from pathlib import Path

# Add parent to path
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from designer_agent import DesignerAgent

async def create_sample_website(path: str):
    """Create a sample website for testing."""
    os.makedirs(path, exist_ok=True)

    # Create a basic HTML website
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TechStart - SaaS Platform</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        .nav { background: #333; padding: 1rem; }
        .nav a { color: white; margin-right: 1rem; text-decoration: none; }
        .hero { background: #f0f0f0; padding: 4rem 2rem; text-align: center; }
        .hero h1 { font-size: 2.5rem; margin-bottom: 1rem; }
        .features { padding: 3rem 2rem; }
        .feature-card { border: 1px solid #ddd; padding: 1.5rem; margin: 1rem; }
        .pricing { padding: 3rem 2rem; background: #fafafa; }
        .pricing-card { border: 2px solid #333; padding: 2rem; margin: 1rem; display: inline-block; }
        .footer { background: #333; color: white; padding: 2rem; text-align: center; }
    </style>
</head>
<body>
    <nav class="nav">
        <a href="#">Home</a>
        <a href="#">Features</a>
        <a href="#">Pricing</a>
        <a href="#">Contact</a>
    </nav>

    <section class="hero">
        <h1>Build Better Software</h1>
        <p>TechStart helps teams collaborate and ship faster with intelligent tools.</p>
        <button>Get Started Free</button>
    </section>

    <section class="features">
        <h2>Powerful Features</h2>
        <div class="feature-card">
            <h3>Real-time Collaboration</h3>
            <p>Work together seamlessly with your team in real-time.</p>
        </div>
        <div class="feature-card">
            <h3>AI-Powered Insights</h3>
            <p>Get intelligent recommendations and analytics.</p>
        </div>
        <div class="feature-card">
            <h3>Enterprise Security</h3>
            <p>Bank-grade security for your sensitive data.</p>
        </div>
    </section>

    <section class="pricing">
        <h2>Simple Pricing</h2>
        <div class="pricing-card">
            <h3>Starter</h3>
            <p>$9/month</p>
            <button>Choose Plan</button>
        </div>
        <div class="pricing-card">
            <h3>Pro</h3>
            <p>$29/month</p>
            <button>Choose Plan</button>
        </div>
        <div class="pricing-card">
            <h3>Enterprise</h3>
            <p>Custom</p>
            <button>Contact Sales</button>
        </div>
    </section>

    <footer class="footer">
        <p>© 2026 TechStart. All rights reserved.</p>
    </footer>
</body>
</html>"""

    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(html_content)

    print(f"✅ Sample website created at: {path}")

async def main():
    """Run the demo."""
    print("=" * 60)
    print("🎨 AutoDesigner Pro - Demo")
    print("=" * 60)

    # Create temporary directories
    with tempfile.TemporaryDirectory() as tmpdir:
        source = os.path.join(tmpdir, "source")
        target = os.path.join(tmpdir, "output")

        # Create sample website
        await create_sample_website(source)

        # Initialize agent
        print("\n🚀 Initializing Designer Agent...")
        agent = DesignerAgent()

        # Run design pipeline
        print("\n⚙️ Running design pipeline...")
        print("-" * 60)

        try:
            context = await agent.design(
                source=source,
                target=target,
                project_id="demo_project",
                auto=True  # Auto-apply for demo
            )

            print("\n" + "=" * 60)
            print("✅ DEMO COMPLETE")
            print("=" * 60)

            print(f"\n📊 Results:")
            print(f"   Keywords found: {len(context.extracted_keywords)}")
            print(f"   Layout type: {context.detected_layout.get('type', 'unknown')}")
            print(f"   Components selected: {len(context.selected_components)}")
            print(f"   Previews generated: {len(context.preview_screenshots)}")

            print(f"\n📁 Output files:")
            for root, dirs, files in os.walk(target):
                level = root.replace(target, '').count(os.sep)
                indent = ' ' * 2 * level
                print(f"{indent}{os.path.basename(root)}/")
                subindent = ' ' * 2 * (level + 1)
                for file in files:
                    print(f"{subindent}{file}")

            print(f"\n🎨 Preview the design:")
            for screenshot in context.preview_screenshots:
                print(f"   Open: {screenshot}")

        except Exception as e:
            print(f"\n❌ Demo failed: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
