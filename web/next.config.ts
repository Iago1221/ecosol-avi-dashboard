import type { NextConfig } from "next";

const repoName = "ecosol-avi-dashboard";

const nextConfig: NextConfig = {
  output: "export",
  basePath: `/${repoName}`,
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
